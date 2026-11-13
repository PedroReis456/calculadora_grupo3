from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from UniRideSite.models import Aluno, Solicitacao, Trajeto


def criar_aluno(nome, email, matricula):
    user = User.objects.create_user(username=email, email=email, password='uniride123')
    return Aluno.objects.create(user=user, nome=nome, email=email, matricula=matricula, curso='Teste')


class ResponderSolicitacaoTests(TestCase):
    '''B5: o motorista aceita ou recusa pedidos da própria carona.'''

    def setUp(self):
        self.motorista = criar_aluno('Mariana', 'mariana@teste.com', '1')
        self.passageiro = criar_aluno('Bernardo', 'bernardo@teste.com', '2')
        self.outro = criar_aluno('Joao', 'joao@teste.com', '3')
        self.trajeto = Trajeto.objects.create(aluno=self.motorista, tipo=Trajeto.OFERECE,
                                              origem='Copacabana', horario='07:00', vagas=1, seg=True)
        self.pedido = Solicitacao.objects.create(trajeto=self.trajeto, passageiro=self.passageiro)
        self.url = reverse('responder-solicitacao', args=[self.pedido.id])

    def responder(self, email, acao):
        self.client.login(username=email, password='uniride123')
        return self.client.post(self.url, {'acao': acao})

    def status(self):
        self.pedido.refresh_from_db()
        return self.pedido.status

    def test_motorista_aceita(self):
        r = self.responder('mariana@teste.com', 'aceitar')
        self.assertRedirects(r, reverse('minhas-caronas'))
        self.assertEqual(self.status(), Solicitacao.ACEITA)

    def test_motorista_recusa(self):
        self.responder('mariana@teste.com', 'recusar')
        self.assertEqual(self.status(), Solicitacao.RECUSADA)

    def test_quem_nao_e_dono_nao_responde(self):
        self.responder('joao@teste.com', 'aceitar')
        self.assertEqual(self.status(), Solicitacao.PENDENTE)

    def test_nao_aceita_sem_vaga(self):
        Solicitacao.objects.create(trajeto=self.trajeto, passageiro=self.outro, status=Solicitacao.ACEITA)
        self.responder('mariana@teste.com', 'aceitar')
        self.assertEqual(self.status(), Solicitacao.PENDENTE)

    def test_pedido_ja_respondido_nao_muda(self):
        self.pedido.status = Solicitacao.RECUSADA
        self.pedido.save()
        self.responder('mariana@teste.com', 'aceitar')
        self.assertEqual(self.status(), Solicitacao.RECUSADA)

    def test_get_nao_e_permitido(self):
        self.client.login(username='mariana@teste.com', password='uniride123')
        r = self.client.get(self.url)
        self.assertEqual(r.status_code, 405)
        self.assertEqual(self.status(), Solicitacao.PENDENTE)

    def test_deslogado_vai_para_login(self):
        r = self.client.post(self.url, {'acao': 'aceitar'})
        self.assertEqual(r.status_code, 302)
        self.assertIn(reverse('login'), r['Location'])
        self.assertEqual(self.status(), Solicitacao.PENDENTE)

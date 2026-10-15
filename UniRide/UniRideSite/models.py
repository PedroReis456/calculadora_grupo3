from django.db import models

# Cada classe abaixo vira uma TABELA no banco de dados.
# Cada atributo da classe vira uma COLUNA da tabela.


class Aluno(models.Model):
    '''
    Estudante da PUC-Rio cadastrado no UniRide.
    Quem tem carro e oferece trajeto atua como motorista;
    quem pede carona atua como passageiro.
    '''
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Entre o nome completo')
    email = models.EmailField(max_length=254, unique=True, help_text='E-mail institucional (@puc-rio.br)')
    matricula = models.CharField(max_length=10, unique=True, help_text='Número de matrícula na PUC-Rio')
    curso = models.CharField(max_length=100, help_text='Curso de graduação')
    membro_desde = models.DateField(auto_now_add=True, verbose_name='Membro desde')

    class Meta:
        managed = True
        db_table = 'Aluno'
        ordering = ['nome']
        verbose_name_plural = 'Alunos'

    def __str__(self):
        '''
        Como o aluno aparece nas listas da página de administração.
        '''
        return "Aluno: " + self.nome
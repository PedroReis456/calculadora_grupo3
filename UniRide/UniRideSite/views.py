from django.contrib.auth import authenticate, login as entrar, logout as deslogar
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from UniRideSite.models import Aluno, Avaliacao, Solicitacao, Trajeto


def login(request):
    '''Tela 1 - Login: confere e-mail e senha e abre a sessão do aluno.'''
    erro = None
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['senha'])
        if user is not None:
            entrar(request, user)
            return redirect('home')
        erro = 'E-mail ou senha incorretos.'
    return render(request, 'login.html', {'erro': erro})


def sair(request):
    '''Encerra a sessão e volta para o login.'''
    deslogar(request)
    return redirect('login')


@login_required
def home(request):
    '''Tela 2 - Início: mostra o trajeto do aluno.'''
    return render(request, 'home.html')


@login_required
def cadastrar_trajeto(request):
    '''Tela 3 - Cadastrar ou editar o trajeto.'''
    return render(request, 'cadastrar-trajeto.html')


@login_required
def caronas_encontradas(request):
    '''Tela 4 - Lista de caronas compatíveis com o trajeto.'''
    caronas = Trajeto.objects.filter(tipo=Trajeto.OFERECE, ativo=True).annotate(
        nota=Avg('aluno__avaliacoes_recebidas__estrelas')
    )
    return render(request, 'caronas-encontradas.html', {'caronas': caronas})

@login_required
def detalhes_carona(request, id):
    '''Tela 5 - Detalhes de uma carona.'''
    carona = get_object_or_404(Trajeto, id=id)
    nota = Avaliacao.objects.filter(avaliado=carona.aluno).aggregate(media=Avg('estrelas'))['media']
    total_caronas = Solicitacao.objects.filter(trajeto__aluno=carona.aluno, status=Solicitacao.ACEITA).count()
    return render(request, 'detalhes-carona.html', {'carona': carona, 'nota': nota, 'total_caronas': total_caronas})


@login_required
def minhas_caronas(request):
    '''Tela 6 - Caronas do aluno (ativas e solicitações).'''
    aluno = aluno_temporario(request)
    return render(request, 'minhas-caronas.html', {'aluno': aluno})


@login_required
def perfil(request):
    '''Tela 7 - Perfil do aluno.'''
    return render(request,'perfil.html')

@login_required
def editar_perfil(request):
    '''Tela 7.1 - Editar perfil: salva nome e curso do aluno.'''
    aluno = aluno_temporario(request)
    if request.method == 'POST':
        aluno.nome = request.POST['nome']
        aluno.curso = request.POST['curso']
        aluno.save()
        return redirect('perfil')
    trajeto = aluno.trajetos.first()
    return render(request, 'editar-perfil.html', {'aluno': aluno, 'trajeto': trajeto})

@login_required
def solicitar_carona(request, id):
    '''Cria um pedido de carona (PENDENTE) para o trajeto escolhido.'''
    carona = get_object_or_404(Trajeto, id=id)
    if request.method == 'POST':
        passageiro = aluno_temporario(request)
        Solicitacao.objects.get_or_create(trajeto=carona, passageiro=passageiro)
    return redirect(reverse('detalhes-carona', args=[id]) + '#enviado')

def termos(request):
    '''Termos de Uso. Página pública: não colocar @login_required (o cadastro aponta para ela).'''
    return render(request, 'termos.html')

def recuperar_senha(request):
    '''Recuperar senha. Página pública: não colocar @login_required.'''
    return render(request, 'recuperar-senha.html')

def aluno_temporario(request):
    '''Devolve o aluno logado (ligado ao usuário do Django).'''
    return request.user.aluno


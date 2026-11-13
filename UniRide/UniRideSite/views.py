from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from UniRideSite.models import Aluno, Avaliacao, Solicitacao, Trajeto
from datetime import datetime
from django.contrib import messages

def login(request):
    '''Tela 1 - Login / Cadastro.'''
    return render(request, 'login.html')


def home(request):
    '''Tela 2 - Início: mostra o trajeto do aluno.'''
    return render(request, 'home.html')


def cadastrar_trajeto(request):
    '''Tela 3 - Cadastrar um trajeto.'''
    if request.method == 'POST':
        aluno = Aluno.objects.get(email='joao@teste.com')
        dias = request.POST.getlist('dias')
        Trajeto.objects.create(
            aluno=aluno,
            tipo=request.POST.get('tipo'),
            origem=request.POST.get('origem'),
            destino=request.POST.get('destino'),
            horario=request.POST.get('horario'),
            vagas=int(request.POST.get('vagas', 0)),
            dom='dom' in dias,
            seg='seg' in dias,
            ter='ter' in dias,
            qua='qua' in dias,
            qui='qui' in dias,
            sex='sex' in dias,
            sab='sab' in dias
        )
        return redirect('home')
    return render(request, 'cadastrar-trajeto.html')

def caronas_encontradas(request):
    '''Tela 4 - Busca de caronas.'''
    caronas = Trajeto.objects.filter(tipo=Trajeto.OFERECE, ativo=True)
    if request.GET.get('origem'):
        caronas = caronas.filter(origem__icontains=request.GET.get('origem'))
    if request.GET.get('horario'):
        caronas = caronas.filter(horario=request.GET.get('horario'))
    if request.GET.get('dia'):
        caronas = caronas.filter(**{request.GET.get('dia'): True})
    return render(request, 'caronas-encontradas.html', {'caronas': caronas})

def detalhes_carona(request, id):
    '''Tela 5 - Detalhes de uma carona.'''
    carona = get_object_or_404(Trajeto, id=id)
    nota = Avaliacao.objects.filter(avaliado=carona.aluno).aggregate(media=Avg('estrelas'))['media']
    total_caronas = Solicitacao.objects.filter(trajeto__aluno=carona.aluno, status=Solicitacao.ACEITA).count()
    return render(request, 'detalhes-carona.html', {'carona': carona, 'nota': nota, 'total_caronas': total_caronas})


def minhas_caronas(request):
    '''Tela 6 - Caronas do aluno (ativas e solicitações).'''
    return render(request, 'minhas-caronas.html')


def perfil(request):
    '''Tela 7 - Perfil do aluno.'''
    return render(request,'perfil.html')

def solicitar_carona(request, id):
    '''Cria um pedido de carona (PENDENTE) para o trajeto escolhido.'''
    carona = get_object_or_404(Trajeto, id=id)
    if request.method == 'POST':
        passageiro = Aluno.objects.get(email='joao@teste.com')  # TEMPORÁRIO: até existir login
        Solicitacao.objects.get_or_create(trajeto=carona, passageiro=passageiro)
    return redirect(reverse('detalhes-carona', args=[id]) + '#enviado')


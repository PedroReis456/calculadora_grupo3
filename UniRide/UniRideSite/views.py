from django.shortcuts import render


def login(request):
    '''Tela 1 - Login / Cadastro.'''
    return render(request, 'login.html')


def home(request):
    '''Tela 2 - Início: mostra o trajeto do aluno.'''
    return render(request, 'home.html')


def cadastrar_trajeto(request):
    '''Tela 3 - Cadastrar ou editar o trajeto.'''
    return render(request, 'cadastrar-trajeto.html')


def caronas_encontradas(request):
    '''Tela 4 - Lista de caronas compatíveis com o trajeto.'''
    return render(request, 'caronas-encontradas.html')


def detalhes_carona(request):
    '''Tela 5 - Detalhes de uma carona.'''
    return render(request, 'detalhes-carona.html')


def minhas_caronas(request):
    '''Tela 6 - Caronas do aluno (ativas e solicitações).'''
    return render(request, 'minhas-caronas.html')


def perfil(request):
    '''Tela 7 - Perfil do aluno.'''
    return render(request,'perfil.html')
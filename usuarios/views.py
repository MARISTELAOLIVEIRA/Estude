from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    # Verifica se o usuário já está logado
    if request.user.is_authenticated:
        messages.add_message(request, constants.INFO, 'Você já está logado')
        return redirect('/flashcard/novo_flashcard/')

    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        user = User.objects.filter(username=username)
        if user:
            messages.add_message(request, constants.ERROR, 'Nome de usuário já existe')
            return redirect('/usuarios/cadastro')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas não conferem')
            return redirect('/usuarios/cadastro')
        
        try:
            User.objects.create_user(
                username=username,
                password=senha
            )
            return redirect('/usuarios/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor')
            return redirect('/usuarios/cadastro')
        
def logar(request):
    # Verifica se o usuário já está logado
    if request.user.is_authenticated:
        messages.add_message(request, constants.INFO, 'Você já está logado')
        return redirect('/flashcard/novo_flashcard/')

    if request.method == "GET":
        print(request.user)
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválido')
            return redirect('/usuarios/logar/')
        
def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.SUCCESS, 'Deslogado!')
    return redirect('/usuarios/logar/')
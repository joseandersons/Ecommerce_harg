from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as django_login

from core.views import user_is_loja
from .models import Loja
from django.contrib.auth import get_user_model




@user_is_loja
def dashboard(request):
    if request.method == 'GET':
        nome_usuario = request.user.username if request.user.is_authenticated else 'Visitante'
        return render(request, 'dashboard.html', {'nome_usuario': nome_usuario})
    else:
        return render(request, 'dashboard.html')
    
def validar_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove qualquer caracter não numérico

    if len(cnpj) != 14:
        return False

    # Calcula o primeiro dígito verificador e compara com o dígito informado
    sum1 = sum(int(a) * b for a, b in zip(cnpj[:-2], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]))
    d1 = 11 - sum1 % 11
    if d1 >= 10:
        d1 = 0

    if int(cnpj[-2]) != d1:
        return False

    # Calcula o segundo dígito verificador e compara com o dígito informado
    sum2 = sum(int(a) * b for a, b in zip(cnpj[:-1], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]))
    d2 = 11 - sum2 % 11
    if d2 >= 10:
        d2 = 0

    if int(cnpj[-1]) != d2:
        return False

    return True


def login_loja(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        User = get_user_model()
        try:
            user = User.objects.get(username=email)
           
        except User.DoesNotExist:
            print(f"No user found with username/email: {email}")
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return render(request, 'login-loja.html')


        if user.check_password(senha):
            if not user.is_loja:
                messages.error(request, 'Este usuário não é uma loja e não pode entrar aqui.')
            else:
                django_login(request, user)
                messages.success(request, 'Você foi logado com sucesso.')
                return redirect('lojas:dashboard')
        else:
            messages.error(request, 'Senha incorreta.')
        
    return render(request, 'login-loja.html')


def logout_loja(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('lojas:login_loja')


def criar_conta_loja(request):
   
    if request.method == "POST":
        
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        senha= request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        complemento = request.POST.get('complemento')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cnpj = request.POST.get('cnpj')
        pausado = request.POST.get('pausado')
        horario_abertura = request.POST.get('horario_abertura')
        horario_fechamento = request.POST.get('horario_fechamento')
        rating = request.POST.get('rating')
        imagem = request.FILES.get('imagem') 
        tipo_culinaria = request.POST.get('tipo_culinaria')
        

        if validar_cnpj(cnpj):
            if Loja.objects.filter(cnpj=cnpj).exists():
                messages.error(request, 'cnpj já cadastrado.')
                return render(request, 'criar-conta-loja.html')
        else:
            messages.error(request, 'cnpj inválido.')
            return render(request, 'criar-conta-loja.html')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'criar-conta-loja.html')
        else:
             senha_confirmada = make_password(senha)

        
        loja = Loja(
            
            username=email,
            first_name=first_name,
            last_name=last_name,
            telefone=telefone,
            email = email,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            password=senha_confirmada, 
            complemento=complemento,
            cidade=cidade,
            estado=estado,
            is_loja = True,
            cnpj=cnpj,
            pausado=pausado,
            horario_abertura=horario_abertura,
            horario_fechamento=horario_fechamento,
            rating=rating,
            imagem=imagem,
            tipo_culinaria=tipo_culinaria

        )
        try:
            loja.save()
        except IntegrityError as e:
            print(f"Integrity Error: {e}")
            messages.error(request, 'Could not save the loja.')
            return render(request, 'criar-conta-loja.html')

        messages.success(request, 'Conta criada com sucesso.')
        return redirect('lojas:login_loja')
    else:
        return render(request, 'criar-conta-loja.html')
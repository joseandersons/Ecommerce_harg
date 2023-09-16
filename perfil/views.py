from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as django_login
from .models import Cliente, Loja
from django.contrib.auth import get_user_model

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


def validador_cpf(cpf):
    # Retira formatação do CPF
    cpf = ''.join(c for c in cpf if c.isdigit())
    
    # Deve conter 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    sum_of_products = sum((int(a) * b) for a, b in zip(cpf[:-2], range(10, 1, -1)))
    expected_digit = 11 - (sum_of_products % 11)
    if expected_digit >= 10:
        expected_digit = 0

    if cpf[-2] != str(expected_digit):
        return False

    # Calcula o segundo dígito verificador
    sum_of_products = sum((int(a) * b) for a, b in zip(cpf[:-1], range(11, 1, -1)))
    expected_digit = 11 - (sum_of_products % 11)
    if expected_digit >= 10:
        expected_digit = 0

    if cpf[-1] != str(expected_digit):
        return False

    return True


def criar_conta_cliente(request):
   
    if request.method == "POST":
        
        username = request.POST.get('username')
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
        senha= request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        complemento = request.POST.get('complemento')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        
        if Cliente.objects.filter(username=username).exists():
            messages.error(request, 'username já cadastrado.')
            return render(request, 'criar-conta-cliente.html')
        
        if validador_cpf(cpf):
            if Cliente.objects.filter(cpf=cpf).exists():
                messages.error(request, 'CPF já cadastrado.')
                return render(request, 'criar-conta-cliente.html')
            cpf_valido = cpf
        else:
            messages.error(request, 'CPF inválido.')
            return render(request, 'criar-conta-cliente.html')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'criar-conta-cliente.html')
        else:
             senha_confirmada = make_password(senha)

        
        cliente = Cliente(
            username=username,
            first_name=first_name,
            last_name=last_name,
            telefone=telefone,
            email = email,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            data_nascimento=data_nascimento,
            cpf=cpf_valido, 
            sexo=sexo,
            password=senha_confirmada, 
            complemento=complemento,
            cidade=cidade,
            estado=estado,
            is_loja = False
        )
        cliente.save()

        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login_cliente')
    else:
        return render(request, 'criar-conta-cliente.html')




def login_cliente(request):
    if request.method == 'POST':
        print("opa2")
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            if user.check_password(senha):
                if user.is_loja:
                    messages.error(request, 'Este usuário é uma loja e não pode entrar aqui.')
                    return render(request, 'login-cliente.html')  # Retornar explicitamente
                else:
                    django_login(request, user)
                    messages.success(request, 'Você foi logado com sucesso.')
                    return redirect('principal')
            else:
                messages.error(request, 'Senha incorreta.')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
        
        return render(request, 'login-cliente.html')
    return render(request, 'login-cliente.html')


def login_loja(request):
    print("login_1")
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print("login_2")
        User = get_user_model()
        try:
            user = User.objects.get(username=email)
            print("login_3")
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
                return render(request, 'dashboard.html')
        else:
            messages.error(request, 'Senha incorreta.')
        
    return render(request, 'login-loja.html')


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
        imagem = request.POST.get('imagem')
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
        return redirect('login_loja')
    else:
        return render(request, 'criar-conta-loja.html')
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from .models import Cliente

def login_cliente(request):
    return render(request, 'login.html')

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
    print("opa")
    if request.method == "POST":
        print("opa2")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
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
            username=first_name,
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
            password=senha_confirmada 
        )
        cliente.save()
        cliente.email

        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login_cliente')
    else:
        return render(request, 'criar-conta-cliente.html')

    
#ex092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

nome = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
cartrab = int(input('Carteira de Trabalho: '))
idade = anonasc - 2002
cadastro = {'nome': nome, 'idade': idade, 'CTPS': cartrab}
if cartrab != 0:
    
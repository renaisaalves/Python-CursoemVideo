#ex092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
nome = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
cartrab = int(input('Carteira de Trabalho: '))
idade = date.today().year - anonasc
if cartrab != 0:
    anocontract = int(input('Ano de contratação: '))
    salario = float(input('Salário (R$): '))
    aposentadoria = idade + 15
cadastro = {'nome': nome, 'idade': idade, 'CTPS': cartrab, 'aposentadoria': aposentadoria, 'ano de contratação': anocontract, 'salário': salario}
print('=' * 30)
print(cadastro)
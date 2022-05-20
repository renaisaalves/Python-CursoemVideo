#ex092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = int(input('Ano de nascimento: '))
cadastro['cartrab'] = int(input('Carteira de Trabalho: '))
idade = date.today().year - cadastro['idade']
if cadastro['cartrab'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
print('=' * 30)
for c, i in cadastro.items():
    print(f'{c} tem o valor {i}')
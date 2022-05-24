#ex094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.

from doctest import NORMALIZE_WHITESPACE


cadastro = dict()
cadastros = list()
while True:
    cadastro['nome'] = str(input('Nome: ')).capitalize().strip()
    cadastro['sexo'] = str(input('Sexo: ')).upper()
    while cadastro['sexo'] not in 'FM':
        cadastro['sexo'] = str(input('Gênero inválido. Digite corretamente [M/F]: ')).upper()
    cadastro['idade'] = int(input('Idade: '))
    while cadastro['idade'] < 0:
        cadastro['idade'] = int(input('Idade incompatível. Digite novamente: '))
    resp = str(input('Quer cadastrar mais alguém? [S/N]: ')).upper()
    cadastros.append(cadastro.copy())
    while resp not in 'SIMSNNÃONAOÑ':
        resp = str(input('Inválido. Digite SIM ou NÃO para confirmar [S/N]: '))
    if resp in 'NNÃONAOÑ':
        break
print(cadastros)
soma = list()
mulher = list()
for c in cadastros:
    soma.append(c['idade'])
    media = sum(soma) / len(cadastros)
    if c['sexo'] in 'F':
        mulher.append(c['nome'])
print('=' * 30)
print(f'A) Ao todo tempos {len(cadastros)} pessoas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulher}')
print(f'D) Lista de pessoas com idade acima da média: ')
print('=' * 30)
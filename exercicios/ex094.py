#ex094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.

cadastro = dict()
cadastros = list()
while True:
    cadastro['nome'] = str(input('Nome: ')).capitalize().strip()
    cadastro['sexo'] = str(input('Sexo: ')).upper()
    if cadastro['sexo'] not in 'FM':
        print('Gênero inválido. Digite corretamente [M/F]: ')
    cadastro['idade'] = int(input('Idade: '))
    if cadastro['idade'] < 0:
        print('Idade incompatível. Digite novamente: ')
    resp = str(input('Quer cadastrar mais alguém? [S/N]: ')).upper()
    if resp not in 'SIMSNNÃONAOÑ':
        print('Inválido. Digite SIM ou NÃO para confirmar [S/N]: ')
    if resp in 'NNÃONAOÑ':
        cadastros.append(cadastro)
        cadastro.clear()
        break
print(cadastros)
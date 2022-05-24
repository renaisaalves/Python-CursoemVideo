#ex094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.

cadastro = dict()

while True:
    cadastro['nome'] = str(input('Nome: ')).capitalize().strip()
    cadastro['sexo'] = str(input('Sexo: ')).upper()
    if cadastro['sexo'] not in 'FM':
        print('Gênero inválido. Digite corretamente [M/F]: ')
    break
        
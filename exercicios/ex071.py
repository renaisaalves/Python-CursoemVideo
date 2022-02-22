#ex071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cont50 = cont20 = cont10 = cont1 = 0
print('=' * 20)
print('BANCO ORIGINAL RA')
print('=' * 20)
valor = int(input('Quanto você deseja sacar? R$: '))
if valor >= 50:
    while valor >= 50:
        valor = valor - 50
        cont50 = cont50 + 1
        if valor < 50:
            while valor >= 20:
                valor = valor - 20
                cont20 = cont20 + 1
            while valor >= 10:
                valor = valor - 10
                cont10 = cont10 + 1
            if valor < 10:
                cont1 = valor 
if valor <= 20:
    while valor >= 20:
        valor = valor - 20
        cont20 = cont20 + 1
    if valor < 20:
        while valor >= 10:
            valor = valor - 10
            cont10 = cont10 + 1
        if valor < 10:
            cont1 = valor
print('-' * 15)
print(f'Saque de R$ {valor}:')
print('-' * 15)
print(f'{cont50} cédulas de R$50.')
print(f'{cont20} cédulas de R$20.')
print(f'{cont10} cédulas de R$10.')
print(f'{cont1} cédulas de R$1.')
print('-' * 15)
print('Fim da operação.')

#ex071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cont50 = 0
print('=' * 20)
print('BANCO ORIGINAL RA')
print('=' * 20)
valor = int(input('Quanto você deseja sacar? R$: '))
while valor > 50:
    valor = valor - 50
    cont50 = cont50 + 1
    if valor < 50:
        resto = valor
print('-' * 15)
print(f'Saque de R$ {valor}:')
print('-' * 15)
print(f'{cont50} cédulas de R$50 e resto R${resto}.')
print('-' * 15)
print('Fim da operação.')

#ex071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

um = 1
dez = 10
vinte = 20
cinquenta = 50
contagem = saque = 0

print('=' * 20)
print('BANCO ORIGINAL RA')
print('=' * 20)
valor = int(input('Quanto você deseja sacar? R$: '))
print('-' * 15)
print(f'Saque de R$ {valor}:')
print('-' * 15)
print(f'{contagem} cédulas de R${um}')
print(f'{contagem} cédulas de R${dez}')
print(f'{contagem} cédulas de R${vinte}')
print(f'{contagem} cédulas de R${cinquenta}')
print('-' * 15)
print('Fim da operação.')

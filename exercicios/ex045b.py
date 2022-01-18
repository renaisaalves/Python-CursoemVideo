#ex45: Crie um programa que faça o computador jogar Jokenpô com você.

#FEITO PELO GUSTAVO GUANABARA

from random import randint
from time import sleep
import emoji

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('''Qual é a sua jogada?
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA
Opção: '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print('*' * 10)
if computador == 0: 
    if jogador == 0:
        print('{}EMPATE!{}' .format('\033[1;33m', '\033[m'))
    elif jogador == 1:
        print('{}VOCÊ VENCEU!{}' .format('\033[1;32m', '\033[m'))
    elif jogador == 2:
        print('{}O COMPUTADOR VENCEU!{}' .format('\033[1;32m', '\033[m'))
    else:
        print('Jogada inválida.')
elif computador == 1:
    if jogador == 0:
        print('{}EMPATE!{}' .format('\033[1;33m', '\033[m'))
    elif jogador == 1:
        print('{}VOCÊ VENCEU!{}' .format('\033[1;32m', '\033[m'))
    elif jogador == 2:
        print('{}O COMPUTADOR VENCEU!{}' .format('\033[1;32m', '\033[m'))
    else:
        print('Jogada inválida.')
elif computador == 2:
    if jogador == 0:
        print('{}EMPATE!{}' .format('\033[1;33m', '\033[m'))
    elif jogador == 1:
        print('{}VOCÊ VENCEU!{}' .format('\033[1;32m', '\033[m'))
    elif jogador == 2:
        print('{}O COMPUTADOR VENCEU!{}' .format('\033[1;32m', '\033[m'))
    else:
        print('Jogada inválida.')
print('*' * 10)
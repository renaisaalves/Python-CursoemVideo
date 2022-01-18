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
print('*' * 20)
if computador == 0: 
    if jogador == 0:
        ambos = 'PEDRA'
        print('{}EMPATE!{}' .format('\033[1;33m', '\033[m'))
        print('Ambos escolheram {}{}{} ' .format('\033[1;33m', ambos, '\033[m'))
    elif jogador == 1:
        print( '{}VOCÊ VENCEU!{}' .format('\033[1;32m', '\033[m'))
    elif jogador == 2:
        print('{}O COMPUTADOR VENCEU!{}' .format('\033[1;31m', '\033[m'))
    else:
        print('Jogada inválida.')
elif computador == 1:
    if jogador == 0: 
        print('{}O COMPUTADOR VENCEU!{}' .format('\033[1;31m', '\033[m'))
    elif jogador == 1:
        print('{}EMPATE!{}' .format('\033[1;33m', '\033[m'))
    elif jogador == 2:
        print('{}VOCÊ VENCEU!{}' .format('\033[1;32m', '\033[m'))
elif computador == 2:
    if jogador == 0:
        print('{}VOCÊ VENCEU!{}' .format('\033[1;32m', '\033[m'))
    elif jogador == 1:
        print('{}O COMPUTADOR VENCEU!{}' .format('\033[1;31m', '\033[m'))
    elif jogador == 2:
        print('{}EMPATE!{}' .format('\033[1;33m', '\033[m'))
print('*' * 20)

#Para usar emoji, substitua o + por 000 e acrescenta \ antes do U.
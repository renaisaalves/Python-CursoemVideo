#ex45: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

opcao = int(input('''Suas opções: 
                    [ 0 ] PEDRA
                    [ 1 ] PAPEL 
                    [ 2 ] TESOURA\nQual é a sua jogada? '''))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
if opcao == computador:
    empate = opcao == computador
    print('{}EMPATOU!{}' .format('\033[1;33m', '\033[m'))
    print('Ambos escolheram {}{}{}' .format('\033[1;33m', empate, '\033[m'))
elif opcao == 0 and computador == 1:
    opcao = 'PEDRA'
    computador = 'PAPEL'
    print('{}VOCÊ PERDEU!{}' .format('\033[1;31m', '\033[m'))
    print('Você escolheu {}{}{} e o Computador escolheu {}{}{}.' .format('\033[1;31m', opcao, '\033[m', '\033[1;32m', computador, '\033[m'))
    print('O papel embrulha a pedra!')
elif opcao == 0 and computador == 2:
    opcao = 'PEDRA'
    computador = 'TESOURA'
    print('{}VOCÊ GANHOU!{}' .format('\033[1;32m', '\033[m'))
    print('Você escolheu {}{}{} e o Computador escolheu {}{}{}' .format('\033[1;32m', opcao, '\033[m', '\033[1;31m', computador, '\033[m'))
    print('A pedra quebra a tesoura!')
elif opcao == 1 and computador == 0:
    opcao = 'PAPEL'
    computador = 'PEDRA'
    print('{}VOCÊ GANHOU!{}' .format('\033[1;32m', '\033[m'))
    print('Você escolheu {}{}{} e o Computador escolheu {}{}{}' .format('\033[1;32m', opcao, '\033[m', '\033[1;31m', computador, '\033[m'))
    print('O papel embrulha a pedra!')
elif opcao == 1 and computador == 2:
    opcao = 'PAPEL'
    computador = 'TESOURA'
    print('{}Você PERDEU!{}' .format('\033[1;31m', '\033[m'))
    print('Você escolheu {}{}{} e o Computador escolheu {}{}{}' .format('\033[1;31m', opcao, '\033[m', '\033[1;32m', computador, '\033[m'))
    print('A tesoura recorta o papel!')
elif opcao == 2 and computador == 1: 
    opcao = 'TESOURA'
    computador = 'PAPEL'
    print('{}Você GANHOU!{}' .format('\033[1;32m', '\033[m'))
    print('Você escolheu {}{}{} e o Computador escolheu {}{}{}' .format('\033[1;32m', opcao, '\033[m', '\033[1;31m', computador, '\033[m'))
    print('A tesoura recorta o papel!')
elif opcao == 2 and computador == 0:
    opcao = 'TESOURA'
    computador = 'PEDRA'
    print('{}Você PERDEU!{}' .format('\033[1;31m', '\033[m'))
    print('Você escolheu {}{}{} e o Computador escolheu {}{}{}' .format('\033[1;31m', opcao, '\033[m', '\033[1;32m', computador, '\033[m'))
    print('A pedra quebra a tesoura!')
else: 
    opcao != 0 or opcao != 1 or opcao != 2
    print('Número inválido.')
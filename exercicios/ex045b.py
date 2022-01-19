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
print('PO!!!\n')
print('*{}*{}' .format('\033[33m', '\033[m') * 25 )
if computador == 0: 
    if jogador == 0:
        empate = 'PEDRA'
        print('{}EMPATE!{}\n' .format('\033[1;33m', '\033[m'))
        print(emoji.emojize('Ambos escolheram {}{}{} :brown_circle:' .format('\033[1;33m', empate, '\033[m')))
    elif jogador == 1:
        print(emoji.emojize(':slightly_smiling_face: {}VOCÊ VENCEU!{}:trophy:\n' .format('\033[1;32m', '\033[m')))
        print('O PAPEL EMBRULHA A PEDRA!\n')
        print(emoji.emojize('Sua escolha: {}{}{} ({}PAPEL{}) :page_with_curl:' .format('\033[1;32m', jogador, '\033[m', '\033[1;32m', '\033[m')))
        print(emoji.emojize('Escolha do computador: {}{}{} ({}PEDRA{}) :brown_circle:' .format('\033[1;31m', computador, '\033[m', '\033[1;31m', '\033[m')))
    elif jogador == 2:
        print(emoji.emojize(':desktop_computer: {}O COMPUTADOR VENCEU!{}:trophy:\n' .format('\033[1;32m', '\033[m')))
        print('A PEDRA QUEBRA A TESOURA!\n')
        print(emoji.emojize('Sua escolha: {}{}{} ({}TESOURA{}) :scissors:' .format('\033[1;31m', jogador, '\033[m', '\033[1;31m', '\033[m')))
        print(emoji.emojize('Escolha do computador: {}{}{} ({}PEDRA{}) :brown_circle:' .format('\033[1;32m', computador, '\033[m', '\033[1;32m', '\033[m')))
    else:
        print('Jogada inválida.')
elif computador == 1:
    if jogador == 0: 
        print(emoji.emojize(':desktop_computer: {}O COMPUTADOR VENCEU!{}:trophy:\n' .format('\033[1;32m', '\033[m')))
        print('O PAPEL EMBRULHA A PEDRA!\n')
        print(emoji.emojize('Sua escolha: {}{}{} ({}PEDRA{}) :brown_circle:' .format('\033[1;31m', jogador, '\033[m', '\033[1;31m', '\033[m')))
        print(emoji.emojize('Escolha do computador: {}{}{} ({}PAPEL{}) :page_with_curl:' .format('\033[1;32m', computador, '\033[m', '\033[1;32m', '\033[m')))
    elif jogador == 1:
        empate = 'PAPEL'
        print('{}EMPATE!{}\n' .format('\033[1;33m', '\033[m'))
        print(emoji.emojize('Ambos escolheram {}{}{} :page_with_curl:' .format('\033[1;33m', empate, '\033[m')))
    elif jogador == 2:
        print(emoji.emojize(':slightly_smiling_face: {}VOCÊ VENCEU!{}:trophy:\n' .format('\033[1;32m', '\033[m')))
        print('A TESOURA RECORTA O PAPEL!\n')
        print(emoji.emojize('Sua escolha: {}{}{} ({}TESOURA{}) :scissors:' .format('\033[1;32m', jogador, '\033[m', '\033[1;32m', '\033[m')))
        print(emoji.emojize('Escolha do computador: {}{}{} ({}PAPEL{}) :page_with_curl:' .format('\033[1;31m', computador, '\033[m', '\033[1;31m', '\033[m')))
elif computador == 2:
    if jogador == 0:
        print(emoji.emojize(':slightly_smiling_face: {}VOCÊ VENCEU!{}:trophy:\n' .format('\033[1;32m', '\033[m')))
        print('A PEDRA QUEBRA A TESOURA!\n')
        print(emoji.emojize('Sua escolha: {}{}{} ({}PEDRA{}) :brown_circle:' .format('\033[1;32m', jogador, '\033[m', '\033[1;32m', '\033[m')))
        print(emoji.emojize('Escolha do computador: {}{}{} ({}TESOURA{}) :scissors:' .format('\033[1;31m', computador, '\033[m', '\033[1;31m', '\033[m')))
    elif jogador == 1:
        print(emoji.emojize(':desktop_computer: {}O COMPUTADOR VENCEU!{}:trophy:\n' .format('\033[1;32m', '\033[m')))
        print('A TESOURA RECORTA O PAPEL!\n')
        print(emoji.emojize('Sua escolha: {}{}{} ({}PAPEL{}) :page_with_curl:' .format('\033[1;31m', jogador, '\033[m', '\033[1;31m', '\033[m')))
        print(emoji.emojize('Escolha do computador: {}{}{} ({}TESOURA{}) :scissors:' .format('\033[1;32m', computador, '\033[m', '\033[1;32m', '\033[m')))
    elif jogador == 2:
        empate = 'TESOURA'
        print('{}EMPATE!{}\n' .format('\033[1;33m', '\033[m'))
        print(emoji.emojize('Ambos escolheram {}{}{} :scissors:' .format('\033[1;33m', empate, '\033[m')))
else: 
    print('Jogada inválida.')
print('*{}*{}' .format('\033[33m', '\033[m') * 25 )

#Para usar emoji, substitua o + por 000 e acrescenta \ antes do U.
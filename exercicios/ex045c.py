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

print('*' * 25 )

if computador == 0: 
    if jogador == 0:
        empate = 'PEDRA'
        print('EMPATE!')
        print('Ambos escolheram {}' .format(empate))
    elif jogador == 1:
        print('VOCÊ VENCEU!')
        print('O PAPEL EMBRULHA A PEDRA!')
        print('Sua escolha: {} (PAPEL)' .format(jogador))
        print('Escolha do computador: {} (PEDRA)' .format(computador))
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
        print('A PEDRA QUEBRA A TESOURA!')
        print('Sua escolha: {} (TESOURA)' .format(jogador))
        print('Escolha do computador: {} (PEDRA)' .format(computador))
    else:
        print('Jogada inválida.')
elif computador == 1:
    if jogador == 0: 
        print('O COMPUTADOR VENCEU!')
        print('O PAPEL EMBRULHA A PEDRA!')
        print('Sua escolha: {} (PEDRA)' .format(jogador))
        print('Escolha do computador: {} (PAPEL)' .format(computador))
    elif jogador == 1:
        empate = 'PAPEL'
        print('EMPATE!')
        print('Ambos escolheram {}' .format(empate))
    elif jogador == 2:
        print('VOCÊ VENCEU!')
        print('A TESOURA RECORTA O PAPEL!')
        print('Sua escolha: {} (TESOURA)' .format(jogador))
        print('Escolha do computador: {} (PAPEL)' .format(computador))
    else: 
        print('Jogada inválida.')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
        print('A PEDRA QUEBRA A TESOURA!\n')
        print('Sua escolha: {} (PEDRA)' .format(jogador))
        print('Escolha do computador: {} (TESOURA)' .format(computador))
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
        print('A TESOURA RECORTA O PAPEL!\n')
        print('Sua escolha: {} (PAPEL)' .format(jogador))
        print('Escolha do computador: {} (TESOURA)' .format(computador))
    elif jogador == 2:
        empate = 'TESOURA'
        print('{}EMPATE!{}')
        print('Ambos escolheram {}')
    else: 
        print('Jogada inválida.')
        
print('*' * 25 )
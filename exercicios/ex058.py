#ex028: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

'''computador = randint(0, 10)
tentativas = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual é o seu palpite? '))
while jogador != computador:
    if computador > jogador:
        tentativas = tentativas + 1
        print('Mais... tente mais uma vez.')
        jogador = int(input('Qual é o seu palpite? '))
    else: 
        computador < jogador
        tentativas = tentativas + 1
        print('Menos... tente mais uma vez.')
        jogador = int(input('Qual é o seu palpite? '))
if jogador == computador:
    print('Você acertou com {} tentativas. Parabéns!' .format(tentativas))'''
    
computador = randint(0, 10)
palpites = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
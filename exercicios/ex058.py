#ex028: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tentativas = 0
computador = randint(0, 3)
print('=' * 30)
print('REMAKE DO JOGO DO DESAFIO 28!')
print('=' * 30)
print('Tente adivinhar o número que o computador escolheu.')
jogador = int(input('Digite um número [0/3]: '))
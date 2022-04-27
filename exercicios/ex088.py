#ex088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint 
from time import sleep

jogos = []
print('=' * 50)
print(f'{"BOLÃO DA MEGA SENA":^50}')
print('=' * 50)
num = int(input('Quantos jogos você quer que eu sorteie?\nRESPOSTA: '))
print('~' * 50)
for c in range(1, num + 1):
    if c > 0:
        jogos.clear()
    for i in range(0, 7):
        sorteio = randint(1, 60)
        jogos.append(sorteio)
        jogos.sort()
        sleep(0.2)
    print(f'{c}º jogo: {jogos}')
print('~' * 50)

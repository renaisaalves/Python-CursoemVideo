#091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

print('=' * 30)
print(f'{"SORTEIO DE DADO":^30}')
print('=' * 30)
numeros = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
for j, n in numeros.items():
    sleep(0.5)
    print(f'O {j} tirou {n}')
print('=' * 30)
print(f'{"RANK DO SORTEIO":^30}')
print('=' * 30)
ranking = list()
ranking = sorted(numeros.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
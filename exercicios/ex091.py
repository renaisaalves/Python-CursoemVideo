#091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

sorteados = list()
sorteio = list()

for c in range(0, 4):
    num = randint(1, 6)
    sorteados.append(num)
numeros = {'jogador1': sorteados[0], 'jogador2': sorteados[1], 'jogador3': sorteados[2], 'jogador4': sorteados[3]}
print(numeros)

for j, n in numeros.items():
    print(f'O {j} acertou {n}')

        
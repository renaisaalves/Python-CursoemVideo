#091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

sorteados = list()

for c in range(0, 4):
    num = randint(1, 6)
    sorteados.append(num)
numeros = {'jogador 1': sorteados[0], 'jogador 2': sorteados[1], 'jogador 3': sorteados[2], 'jogador 4': sorteados[3]}
print(numeros)

            
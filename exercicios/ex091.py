#091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
resultado = dict()

jogador = randint(1, 6)
resultado = {'jogador1': jogador}
print(resultado)
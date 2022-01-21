#ex049: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
from stringprep import c9_set


n = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    tabuada = n * c
    cont = c
    print('{} x {} = {}' .format(n, c, tabuada))


#AULA 8: USANDO MÓDULOS DO PYTHON

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de um {} é igual a {}' .format(num, raiz))

import emoji
print(emoji.emojize("Olá, Mundo! :heart:", use_aliases=True))

#Sempre que eu quiser instalar uma biblioteca, basta ir no TERMINAL e escrever pip install nome da biblioteca
#Caso queira saber a lista de bibliotecas já instaladas, basta digitar pip list no TERMINAL. 
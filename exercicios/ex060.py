#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.' .format(n, f))

n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
print('Calculando {}! = ' .format(c), end='')
while c > 0:
    print('{}' .format(c), end=' ')
    print('x' if c > 1 else '=', end= ' ')
    c = c - 1
print('O fatorial de {} é {}.' .format(n, f))


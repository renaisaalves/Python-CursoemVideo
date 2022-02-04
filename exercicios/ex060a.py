#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

n = int(input('Digite um número: '))
c = n
while c > 0:
    print('{}' .format(c), end=' ')
    print('x' if c > 1 else '=', end= ' ')
    c = c - 1
print('O fatorial de {} é {}.' .format(n, f))

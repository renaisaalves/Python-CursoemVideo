#ex074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

#NÃO CONSEGUI FAZER, PORQUE NÃO SEI COLOCAR DENTRO DE UMA TUPLA

num = (58, 77, 18, 9, 16)
print(sorted(num))
print(f'Menor número: {num[0]}')
print(f'Maior número: {num[4]}')
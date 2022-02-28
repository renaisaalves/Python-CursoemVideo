#ex074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

#NÃO CONSEGUI FAZER, PORQUE NÃO SEI COLOCAR DENTRO DE UMA TUPLA

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os números:', sorted(num))
print(f'Menor número: {sorted(num)[0]}')
print(f'Maior número: {sorted(num)[4]}')

#OUTRA FORMA DE MOSTRAR O MENOR E MAIOR NÚMERO DA TUPLA:

for n in num:
    print(f'{n}', end=' ')
print(f'\nO menor valor sorteado foi {min(num)}')    
print(f'O maior valor sorteado foi {max(num)}')

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
total = 0

for c in range(1, n + 1):
    if n % c == 0:
        total = total + 1 
        print('\033[33m', c,'\033[m', end=' ')
    else:
        print('\033[31m', c, '\033[m', end=' ')
print('\nO número {} foi dividido {} vezes.' .format(n, total))
if  total == 2:
    print('E por isso ele é PRIMO!')
else: 
    print('E por isso ele NÃO É PRIMO!')
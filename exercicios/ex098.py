#ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

from time import sleep

def contador(i, f, p):
    print('=' * 40)
    print(f'Contagem de 1 até 10 [de 1 em 1]:')
    for c in range(1, 10+1):
        print(f'{c} ', end='')
    print()
    print('=' * 40)
    print(f'Contagem de 10 até 0 [de 2 em 2]:')
    for u in range(10, 0, -1):
        if u % 2 == 0:
            print(f'{u} ', end='')
    print()
    print('=' * 40)
    print(f'Contagem personalizada:')
    for k in range(i, f, p):
        print(f'{k} ', end='')
        print()
contador(3, 5, 7)        
print('Agora é a sua vez de realizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))



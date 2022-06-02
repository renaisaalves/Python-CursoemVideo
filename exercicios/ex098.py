#ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def contador(i, f):
    print('=' * 30)
    print(f'Contagem de 1 até 10 [de 1 em 1]')
    for i in range(1, 10+1):
        print(f'{i} ', end='')
    print()
    print('=' * 30)
    print(f'Contagem de 10 até 0 [de 2 em 2]')
    for f in range(1, 10+1):
        if f % 2 == 0:
            print(f'{f} ', end='')
    print()
    print('=' * 30)
contador(0, 3)
    
    

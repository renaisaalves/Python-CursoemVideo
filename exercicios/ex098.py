#ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def contador():
    print('=' * 30)
    print(f'Contagem de 1 até 10 [de 1 em 1]')
    for v in range(1, 10+1):
        print(f'{v} ', end='')
    print()
    print('=' * 30)
    print(f'Contagem de 10 até 0 [de 2 em 2]')
    for u in range(10, 0, -1):
        if u % 2 == 0:
            print(f'{u} ', end='')
    print()
    print('=' * 30)
contador()


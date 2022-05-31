#ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def contador(i, f):
    for i in range(0, 10, 1):
        print(f'Contagem inicio: {i}')
    for f in range(0, 10, -1):
        if f % 2 == 0:
            print(f'Contagem fim: {f}')
contador(1, 3)
    

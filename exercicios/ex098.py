#ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    for c in range(i, f, p):
        print(f'{c} ', end='')
    print('FIM!')
contador(1, 10, 1)


#ex098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i <= f:
        cont = 1
        while i <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM!')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('FIM!')
contador(1, 10, 1)


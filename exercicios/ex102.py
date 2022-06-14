#ex102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    if show == True:
        for c in range(n-1, 0, -1):
            if c == n-1:
                fat = n * c
                print(f'{n} ', end='')
            else:
                fat *= c
                print(f'x {c} ', end='')
    print(f'= {fat}')
fatorial(4, show=False)
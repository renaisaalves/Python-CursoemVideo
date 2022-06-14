#ex102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n):
    for c in range(n, 0, -1):
        if c == n:
            fat = n * n-1
        if c < n:
            fat = fat * n-1
        print(f'{n} ', end='')
fatorial(4)
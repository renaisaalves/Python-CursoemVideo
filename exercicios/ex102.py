#ex102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n):
    for c in range(n, 0, -1):
        print(c , end='')
fatorial(4)

# n é um número qualquer a ser digitado pelo usuário. 
# eu peguei como exemplo o número 4. 
# no fatorial, o número 4 precisa dar como resultado 24. 
# a ideia é que haja uma multiplicação em ordem decrescente, até chegar no valor. 
# 
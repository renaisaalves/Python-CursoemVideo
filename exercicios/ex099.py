#ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(valor):
    valor.sort(reverse=True)
    print(f'O maior valor é {valor[0]}')
maior([3, 5, 10, 4, 2, 6])



#ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(m):
    for c in range(len(m)):
        if c == 0:
            print('Deu certo')
values = [10, 7, 2, 14, 8]
maior(values)

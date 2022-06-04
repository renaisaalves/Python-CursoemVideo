#ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(values):
    pass

inteiros = list()
while True:
    inteiros.append(int(input('Número: ')))
    resp = str(input('Quer adicionar mais algum número? [S/N]: ')).upper()[0]
    if resp in 'N':
        break
print(inteiros)
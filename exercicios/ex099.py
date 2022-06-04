#ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* valor):
    tamanho = len(valor)
    print(f'Recebi os valores {valor} e são ao todo {tamanho}')
maior(3, 4, 8)
maior(5, 2)
#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def linha(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)
linha('CALCULANDO TERRENO RETANGULAR')

def area(l, c):
    total = l * c
    print(f'A área total do terreno {l}x{c} é de {total}m²')
    
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}' .format(hi))'''


#Fazendo com a importação da biblioteca math completa: 

'''import math 
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))'''

#Fazendo apenas com a importação de um item específico da biblioteca math:

from math import hypot 

co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))
#ex016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''from math import trunc

num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}.' .format(num, trunc(num)))'''

#Quando utiliza import math, em .format deve ser especificado math.algumacoisa
#Do contrário, quando queremos utilizar apenas um item de math, não precisamos utilizar math. Basta escrever direto o nome do item (ex: trunc).

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.' .format(num, int(num)))

#Mas nem sempre precisa importar biblioteca. No exemplo acima, apenas trocamos o item trunc pelo int (inteiro).
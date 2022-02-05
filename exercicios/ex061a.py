#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#FEITO POR MIM

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = 0
while termo != 10:
    termo = termo + 1
    an = a1 + (termo - 1) * r
    print('➝ ', an, end=' ')
else:
    termo == 10
    print('\nFim do Programa.')
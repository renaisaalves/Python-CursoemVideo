#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date 
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual.'))
if ano == 0:
    ano = date.today().year #módulo para o Python olhar seu ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO' .format(ano))
else:
    print('O ano {} NÃO é BISSEXTO' .format(ano))
    
# != : diferente
# and : e 
# or : ou

#Resolução do problema: Se o resto da divisão (%) por 4 for igual (==) a 0 e o resto da divisão (%) por 100 for diferente (!=) de zero ou o resto da divisão (%) por 400 for igual (==) a 0, então exiba na tela... 
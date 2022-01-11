#ex039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc 

if idade < 18:
    diferenca = 18 - idade 
    falta = date.today().year + diferenca
    print('De acordo com a sua idade ({}), você ainda vai alistar no Serviço Militar.' .format(idade))
    print('Falta(m) {} ano(s) para você se alistar.' .format(diferenca))
    print('O seu alistamento está previsto para ser em \033[1;32m{}\033[m.' .format(falta))
elif idade == 18:
    print('De acordo com a sua idade ({}), já está na hora exata de se alistar no Serviço Militar.' .format(idade))
else:
    diferenca = idade - 18
    falta = date.today().year - diferenca
    print('De acordo com a sua idade ({}), já passou do tempo do seu alistamento no Serviço Militar.' .format(idade))
    print('A idade para se alistar é de 18 anos. Já se passou \033[1;31m{}\033[m ano(s) que você não se alistou.' .format(diferenca))
    print('O seu alistamento deveria ter sido em \033[1;31m{}\033[m.' .format(falta))

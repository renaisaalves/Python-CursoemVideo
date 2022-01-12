#ex034: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM 
#Até 14 anos: INFANTIL 
#Até 19 anos: JÚNIOR 
#Até 25 anos: SÊNIOR 
#Acima de 25 anos: MASTER

from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Você tem {} anos.\nSua categoria é {}MIRIM{}.' .format(idade, '\033[1;31m', '\033[m'))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos.\nSua categoria é {}INFANTIL{}.' .format(idade, '\033[1;33m', '\033[m'))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos.\nSua categoria é {}JÚNIOR{}.' .format(idade, '\033[1;32m', '\033[m'))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos.\nSua categoria é {}SÊNIOR{}.' .format(idade, '\033[1;34m', '\033[m'))
else:
    idade > 25
    print('Você tem {} anos.\nSua categoria é {}MASTER{}.' .format(idade, '\033[1;36m', '\033[m'))
    
    #TEM UMA MANEIRA MAIS PRÁTICA DE FAZER ISSO sem usar operador lógico. Basta escrever idade <= x
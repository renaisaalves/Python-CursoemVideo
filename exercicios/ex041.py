#ex034: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM 
#Até 14 anos: INFANTIL 
#Até 19 anos: JÚNIOR 
#Até 25 anos: SÊNIOR 
#Acima de 25 anos: MASTER

nasc = int(input('Digite seu ano de nascimento: '))
if nasc <= 9:
    print('Sua categoria é {}MIRIM{}.' .format('\033[1;31m', '\033[m'))
elif nasc <= 14:
    print('Sua categoria é {}INFANTIL{}.' .format('\033[1;33m', '\033[m'))
elif nasc <= 19:
    print('Sua categoria é {}JÚNIOR{}.' .format('\033[1;32m', '\033[m'))
elif nasc <= 25:
    print('Sua categoria é {}SÊNIOR{}.' .format('\033[1;34m', '\033[m'))
else:
    nasc > 25
    print('Sua categoria é {}MASTER{}.' .format('\033[1;36m', '\033[m'))
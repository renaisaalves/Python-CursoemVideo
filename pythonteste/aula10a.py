#AULA 10: CONDIÇÃO

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 10:
    print('Carro novo')
else: 
    print('Carro velho')
print('--FIM--')

#Eu também posso escrever assim:

#tempo = int(input('Quantos anos tem seu carro? '))
#print('carronovo' if tempo <=3 else 'carrovelho')
#print('--FIM--') 

#Mas não gosto desse método. Prefiro o primeiro.

nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Gustavo':
    print('Seu nome é tão comum.')
else: 
    print('Que nome lindo você tem!')
print('Bom dia {}!' .format(nome))


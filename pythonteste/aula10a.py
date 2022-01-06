#AULA 10: CONDIÇÃO SIMPLES E COMPOSTA

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
if nome == 'Renaísa':
    print('Que nome lindo você tem!')
else: 
    print('Seu nome é tão comum.')
print('Bom dia {}!' .format(nome))

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: {}' .format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim! Estude novamente')
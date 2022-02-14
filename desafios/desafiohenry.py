#1 - Escreva um programa em Python que pede ao utilizador que lhe forneça dois números (x e y) e que
#escreve o valor de (x + 3 * y) * (x - y). O seu programa deve gerar uma interação como a seguinte:
#Vou pedir-lhe dois números
#Escreva o primeiro número, x =5
#Escreva o segundo número, y=6
#O valor de (x + 3 * y) * (x - y) é: -23

'''x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
valor = (x + 3 * y) * (x - y)
print('O valor de', (x + 3 * y) * (x - y), 'é: ', valor)'''

#2 - Escreva um programa em Python que lê os valores correspondentes a uma distância percorrida (em Km) e o tempo necessário para a percorrer (em minutos), e calcula a velocidade média em:
#a. Km /h
#b. m/s

'''km = float(input('Informe a distância: '))
minutos = int(input('Tempo em minutos: '))
horas = minutos / 60 
vm = km / horas 
ms = vm * 3.6
print('~' * 30)
print('Velocidade média:', vm,'km/h')
print('Tempo em horas {:.2f} h' .format(horas))
print('Velocidade média:', ms, 'm/s')
print('~' * 30)'''

#Escreva um programa em Python que pede ao utilizador que lhe forneça um inteiro correspondente a um número de segundos e que calcula o número de dias correspondentes a esse número em segundos. O seu programa deve permitir a interação: um dia tem 86400 segundos

'''numero = int(input('Escreva um número em segundos: '))
dia = 86400
resultado = numero / dia 
print('*' * 40)
print('O número de dias correspondentes é:', resultado)
print('*' * 40)'''


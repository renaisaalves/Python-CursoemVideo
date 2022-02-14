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

#3 - Escreva um programa em Python que pede ao utilizador que lhe forneça um inteiro correspondente a um número de segundos e que calcula o número de dias correspondentes a esse número em segundos. O seu programa deve permitir a interação: um dia tem 86400 segundos

'''numero = int(input('Escreva um número em segundos: '))
dia = 86400
resultado = numero / dia 
print('*' * 40)
print('O número de dias correspondentes é:', resultado)
print('*' * 40)'''

#4 - Escreva um número que lê um número inteiro correspondente a um certo número de segundos e que escreve o número de dias, horas, minutos e segundos correspondentes a esse número. Por exemplo: Escreva o número de segundos 345678 dias: 4 horas: 0 mins: 1 segs: 18

#5 - Escreva um programa em Python que lê três números e que diz qual o maior dos números lidos

#6 - Escreva um programa em Python que pede ao utilizador que lhe forneça um número correspondente a um ano e que indica se o ano é bissexto. Um ano é bissexto se for divisível por 4 e não for divisível por 100, a não ser que seja também divisível por 400. Por exemplo, 1984 é bissexto, 1100 não é, e 2000 é bissexto. O seu programa deve gerar uma interação como a seguinte: Escreva um ano para eu dizer se é bissexto Ano -> 1984 O ano 1984 é bissexto

#7 - Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal tendo em conta as horas extraordinárias. O salário é calculado do seguinte modo: se o número de horas for menor que 40, então o salário é dado pelo produto do número de horas pelo salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar. 

#8 - Escreva um programa em Python que lê um número inteiro positivo e calcula o número obtido do número lido que apenas contém os seus dígitos ímpares. Por exemplo, Escreva um inteiro ? 785554 Resultado: 7555

#9. Escreva um programa em Python que lê um número inteiro positivo e produz o número correspondente a inverter a ordem dos seus dígitos. Por exemplo, Escreva um inteiro positivo ? 7633256 O número invertido é 6523367

#10. Escreva um programa em Python que pede ao utilizador que lhe forneça um número e que escreve a tabuada da multiplicação para esse número.

#11. Escreva um programa que lê um número inteiro e determina quantas vezes aparecem dois zeros seguidos. Por exemplo, Escreva um inteiro ? 98007640003 O número tem 3 zeros seguidos







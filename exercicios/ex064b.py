#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = soma = 0 #NOVIDADE: SHORTHAND DE VÁRIAS VARIÁVEIS RECEBENDO O MESMO VALOR
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.' .format(cont, soma))
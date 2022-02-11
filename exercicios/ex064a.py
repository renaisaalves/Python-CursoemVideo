#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

#FEITO POR MIM

soma = 0
n2 = 0
n = 0
while n != 999: 
    n = int(input('Digite um número: '))
    soma = soma + 1
    n1 = n 
    n3 = n1 + n2
    n2 = n3
print('No total, {} números foram digitados.' .format(soma - 1))
print('A soma entre os números foi {}.' .format(n3 - n))


# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

#MEU CÓDIGO

soma = contador = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    contador = contador + 1
    soma = soma + n
print(f'Ao todo, {contador} números foram digitados.\nA soma entre eles foram {soma}.')

#CÓDIGO GUANABARA

soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont = cont + 1 
    soma = soma + n
print(f'A soma dos {cont} valores foi {soma}.')





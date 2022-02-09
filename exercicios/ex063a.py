# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

contagem = 0
valor1 = 0
valor2 = 1
print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)
termos = int(input('Quantos termos você quer mostrar? '))

while contagem != termos:
    contagem = contagem + 1
 
    print(resultado, '–', end=' ')
print('FIM.')

# 1 = 0 + 1
# 2 = 1 + 1  
# 3 = 2 + 1
# 5 = 2 + 3
# 8 = 5 + 3 
# 13 = 8 + 5 
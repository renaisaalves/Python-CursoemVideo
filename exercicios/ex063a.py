# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

contagem = 0
valor1 = 1
valor2 = 0
resultado = 0
print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)
termos = int(input('Quantos termos você quer mostrar? '))

while contagem != termos:
    contagem = contagem + 1
    resultado = valor1 + valor2
    valor2 = valor1
    valor1 = resultado
    print(resultado, '–', end=' ')
print('FIM.')

# 1 = 1 + 0
# 2 = 1 + 1  
# 3 = 2 + 1
# 5 = 3 + 2 
# 8 = 5 + 3 
# 13 = 8 + 5 
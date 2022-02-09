# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

#FEITO POR MIM

contagem = 0
valor1 = 1
valor2 = 0
resultado = 0
print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
# print(resultado, end=' ')

#OPÇÃO 1 (A RESOLVER)
while contagem != termos:
    contagem = contagem + 1
    if contagem == 1:
        print(resultado, '➞ ', end=' ')
    if contagem == 2:
        print(resultado, '➞ ', end=' ')
    resultado = valor1 + valor2
    valor2 = valor1
    valor1 = resultado
    print(resultado, '➞ ', end=' ')
print('FIM.')

#OPÇÃO 2 
'''print(resultado, '➞ ', end=' ')
print(resultado + 1, '➞ ', end=' ')
while contagem != termos:
    contagem = contagem + 1
    resultado = valor1 + valor2
    valor2 = valor1
    valor1 = resultado
    print(resultado, '➞ ', end=' ')
print('FIM.')'''
#ex038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

#FEITO POR MIM

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro valor ({}) é \033[1;32mmaior\033[m que o segundo valor ({}).' .format(n1, n2))
elif n2 > n1:
    print('O segundo valor ({}) é \033[1;32mmaior\033[m que o primeiro valor ({}).' .format(n2, n1))
else: 
    n1 == n2
    print('Não existe valor maior, pois \033[1;33mambos\033[m são iguais.')

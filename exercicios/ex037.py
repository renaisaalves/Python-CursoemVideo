#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#INCOMPLETO 

numero = int(input('Digite um número: '))
print('''Qual base de conversão você quer? 
      [ 1 ] Binário 
      [ 2 ] Octal 
      [ 3 ] Hexadecimal.''')
escolha = int(input('Sua escolha: '))

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}' .format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}' .format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}' .format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')
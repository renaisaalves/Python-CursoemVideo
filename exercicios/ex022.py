#ex022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Qual é o seu nome completo?\n')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é: {}' .format(nome.upper()))
print('Seu nome em minúsculo é: {}' .format(nome.lower()))
print('Seu nome ao todo tem {} letras.' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.' .format(nome.find(' '))) # ou então posso fazer assim:
nomeseparado = nome.split()
print(nomeseparado)
print('Seu primeiro nome é {} e ele tem {} letras.' .format(nomeseparado[0], len(nomeseparado[0])))
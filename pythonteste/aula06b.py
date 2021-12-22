#AULA 6: TIPOS PRIMITIVOS E SAÍDA DE DADOS 

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} vale {}' .format(n1, n2, s))

n = bool(input('Digite um valor: '))
print(type(n))

n = input('Digite algo: ')
print(n.isnumeric())

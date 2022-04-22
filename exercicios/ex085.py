#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

from sqlite3 import paramstyle


valor = list()
par = list()
impar = list()

print('=' * 50)
print(f'{"FILTRANDO NÚMEROS NA LISTA":^50}')
print('=' * 50)
for i in range(1, 8):
    valor.append(int(input(f'Digite o {i}º valor: ')))
valor.sort()
for n in valor:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
valor.clear()
valor.append(par)
valor.append(impar)
print(('=' * 50))
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
print(f'Lista gerada: {valor}')
(print('=' * 50))

#Dica: quando você quer criar várias listas dentro de uma, você já pode declarar na seguinte forma: 
# [[], []]
#Supondo que você queira colocar algum valor na lista da esquerda, basta vc escrever o nome da lista maior (que está englobando as duas listas) informando o índice da lista esquerda e depois adicionar esse valor, ex: exemplo[1].append(valor)

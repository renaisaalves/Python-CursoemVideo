#ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for c in range(1, 6):
    valores.append(int(input(f'Digite o {c}º valor: ')))
print(f'Valores digitados: {valores}')
valores.sort()
print(f'Menor valor: {valores[0]}')
print(f'Maior valor: {valores[4]}')



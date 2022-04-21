#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valor = list(int)
impar = list(int)
e = '\033[m' #fechando as cores

for i in range(1, 8):
    valor.append(int(input(f'Digite o {i}º valor: ')))
print(valor)

for c in valor:
    if c % 2 == 1:
        valor.remove(c)
        impar.append(c)
print('=' * 30)
print(f'Números ímpares: {impar}.')
print(f'Lista completa: {valor}')
print('=' * 30)
#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valor = list()
par = list()
impar = list()

for i in range(1, 8):
    valor.append(int(input(f'Digite o {i}º valor: ')))
valor.sort()
for n in valor:
    if n % 2 == 1:
        impar.append(n)
    else:
        par.append(n)
valor.clear()
valor.append(par)
valor.append(impar)
print(('=' * 30))
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
print(f'Lista gerada: {valor}')
(print('=' * 30))

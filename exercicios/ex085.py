#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valor = list()
par = list()
impar = list()

for i in range(1, 8):
    valor.append(int(input(f'Digite o {i}º valor: ')))
valor.sort()

for c in valor:
    if c % 2 == 1:
        impar.append(c)
        valor.remove(c)
        for h in impar:
            valor.append(h)
print(('=' * 30))
print(f'Números ímpares: {impar}')
print(f'Lista gerada: {valor}')
(print('=' * 30))

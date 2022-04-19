#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valor = list()
par = list()

for i in range(1, 8):
    valor.append(int(input(f'Digite o {i}º valor: ')))

print(valor)
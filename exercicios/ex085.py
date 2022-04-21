#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valor = list()
a = '\033[1;33m' #a de amarelo
v = '\033[1;32m' #v de  verde
e = '\033[m' #fechando as cores

for i in range(1, 8):
    valor.append(int(input(f'Digite o {i}º valor: ')))
print(valor)

for c in valor:
    if c % 2 == 1:
        valor.append(c)
        valor.remove(c)
print('=' * 30)
print(f'Em amarelo representa todos os números {a}pares{e}.')
print(f'Em verde, todos os números {v}ímpares{e}.')
print('=' * 30)
print(valor)

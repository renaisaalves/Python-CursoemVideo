#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valor = list()
a = '\033[1;31m' #a de amarelo
v = '\033[1;32m' #v de  verde
e = '\033[m' #fechando as cores

for i in range(1, 8):
    valor.append(int(input(f'Digite o {i}º valor: ')))
for c in valor:
    if c % 2 == 1:
        valor.remove(c)
        valor.append(c)
print(f'Em amarelo representa todos os números {a}pares{e}.\n Em verde, todos os números {v}ímpares{e}.')
print(valor)

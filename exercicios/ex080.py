#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

#NÃO CONSEGUI FAZER

for c in range(0, 2):
    lista.append(int(input(f'Digite o {c}º valor: ')))
    if c > 0:
        if lista[0] > lista[1]:
            lista.insert(0, [1])
print(f'{lista}')
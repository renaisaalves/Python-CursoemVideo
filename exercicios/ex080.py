#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for c in range(0, 6):
    val = int(input(f'Digite o {c}º valor: '))
    if c == 0:
        val1 = val
    if val1 > val:
        
print(f'{lista}')
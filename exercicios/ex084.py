#ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

cadastro = list([''], [''], [''], [''])

for i in cadastro:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    cadastro.append(nome)
    cadastro.append(peso)
    break
print(cadastro)
print(cadastro[0][0])
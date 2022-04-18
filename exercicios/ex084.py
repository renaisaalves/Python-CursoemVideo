#ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

cadastro = []
listagem = list()
total = 0

while True:
    cadastro.append(str(input('Nome: ')).capitalize())
    cadastro.append(int(input('Peso: ')))
    listagem.append(cadastro[:])
    cadastro.clear()
    total += 1
    resposta = str(input('Quer continuar? [Sim/Não]: ')).upper()
    if resposta not in 'SIMS':
        break
print(listagem)
print(f'{total} pessoas foram cadastradas.')
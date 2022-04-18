#ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

cadastro = []
total = 0

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    peso = int(input('Peso: '))
    cadastro.append(nome)
    cadastro.append(peso)
    total += 1
    resposta = str(input('Quer continuar? [Sim/Não]: ')).upper()
    if resposta not in 'SIMS':
        break
print(cadastro)
print(f'{total} pessoas foram cadastradas.')
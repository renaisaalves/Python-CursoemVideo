#ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

# NÃO CONSEGUI FAZER 

cadastro = []
listagem = list()
total = 0

while True:
    cadastro.append(str(input('Nome: ')).capitalize())
    cadastro.append(int(input('Peso: ')))
    listagem.append(cadastro[:]) #a listagem fez uma cópia da lista anterior. Isso é fundamental.
    cadastro.clear()
    resposta = str(input('Quer continuar? [Sim/Não]: ')).upper()
    if resposta not in 'SIMS':
        break
    
print('=' * 30)
print(f'{len(listagem)} pessoas foram cadastradas:')
print(listagem)
print('=' * 30)
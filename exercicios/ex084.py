#ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

cadastro = []
listagem = list()
total = 0

while True:
    cadastro.append(str(input('Nome: ')).capitalize())
    cadastro.append(int(input('Peso: ')))
    listagem.append(cadastro[:]) #a listagem fez uma cópia da lista anterior. Isso é fundamental.
    cadastro.clear()
    total += 1
    resposta = str(input('Quer continuar? [Sim/Não]: ')).upper()
    if resposta not in 'SIMS':
        break

for i in listagem:
    if i[1] >= 60:
        print(f'{i[0]} é o mais pesado.')
    else:
        print(f'{i[0]} é o mais leve.')
        
print('=' * 30)
print(f'{total} pessoas foram cadastradas:')
print(listagem)
print('=' * 30)

#ALGORITMO

#Eu preciso fazer com que cada peso i[1] seja comparado com o outro valor. 


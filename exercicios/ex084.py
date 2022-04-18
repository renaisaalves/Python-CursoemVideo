#ex084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

# NÃO CONSEGUI FAZER 

cadastro = []
listagem = list()
maior = menor = 0

while True:
    cadastro.append(str(input('Nome: ')).capitalize())
    cadastro.append(int(input('Peso: ')))
    if len(listagem) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    listagem.append(cadastro[:]) #a listagem fez uma cópia da lista anterior. Isso é fundamental.
    cadastro.clear()
    resposta = str(input('Quer continuar? [Sim/Não]: ')).upper()
    if resposta not in 'SIMS':
        break
    
print('=' * 30)
print(f'{len(listagem)} pessoas foram cadastradas:')
print(f'O maior peso foi de {maior}kg. ')
print(f'O menor peso foi de {menor}kg. ')
print(listagem)
print('=' * 30)

for i in listagem:
    if i[1] == maior:
        print(f'{i[0]} é o maior.')
    else:
        print(f'{i[0]} é o menor.')
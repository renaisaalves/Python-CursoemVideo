#ex082: Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

generico = []
pares = []
impares = []
resposta = 'SIMSSS'

while resposta in 'SIMSSS':
    generico.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resposta not in 'SIMSSS':
        for c, v in enumerate(generico):
            if v % 2 == 0:
                pares.append(v)
            else:
                impares.append(v)
        break
print('=' * 30)
print(f'Todos os números digitados: {generico}')
print(f'Somente números pares: {pares}')
print(f'Somente números ímpares: {impares}')
print('=' * 30)
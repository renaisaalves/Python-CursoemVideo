#ex082: Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

generico = []
resposta = 'SIMSSS'

while resposta in 'SIMSSS':
    generico.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resposta not in 'SIMSSS':
        print(f'{generico}')
        break
        
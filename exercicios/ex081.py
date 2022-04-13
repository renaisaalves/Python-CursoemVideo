#ex 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
resposta = 'SIMS'

while resposta in 'SIMS':
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()
    if resposta not in 'SIMS':
        cont = len(lista)
        lista.sort(reverse=True)
        num = int(input('Qual número você quer encontrar? '))
        break
print('=' * 50)
print(f'Lista em ordem decrescente: {lista}')
print(f'Foram digitados {cont} números.')   
if num in lista:
    frequencia = lista.count(num)
    print(f'O valor {num} foi digitado {frequencia} vezes e está na lista.')
else:
    print(f'O valor {num} não foi digitado e não está na lista.')
print('=' * 50)
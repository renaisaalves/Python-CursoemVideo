#ex 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
resposta = 'SIMS'

while resposta in 'SIMS':
    num = int(input('Digite um número: '))
    lista.append(num)
    resposta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()
    if resposta not in 'SIMS':
        cont = len(lista)
        lista.sort(reverse=True)
        print('=' * 50)
        print(f'Foram digitados {cont} números.')
        if 5 in lista:
            frequencia = lista.count(5)
            print(f'O valor 5 foi digitado {frequencia} vezes e está na lista.')
        else:
            print(f'O valor 5 não foi digitado e não está na lista.')
        print('=' * 50)
        break
print(f'Lista em ordem decrescente: {lista}')
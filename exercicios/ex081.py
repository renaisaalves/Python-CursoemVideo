#ex 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0

repeat = int(input('Quantas vezes você quer repetir? '))
while not repeat:
    cont += 1
    number = int(input(f'Número {cont}: '))
    lista.append(number)
    if cont == repeat:
        resposta = str(input('Deseja continuar? Sim/Não')).strip().upper()
        if resposta in 'NNÃONAO':
            break
print('=' * 40)
print(f'Sua lista: {lista}')
print(f'Foram digitados {c} números.')
print(f'Em ordem crescente: {lista.sort()}')
print(f'Em ordem decrescente: {lista.sort(reverse=True)}', )
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista.')
else:
    print(f'O valor 5 não foi digitado e não está na lista.')
print('=' * 40)
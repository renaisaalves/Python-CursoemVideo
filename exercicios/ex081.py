#ex 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

repeat = int(input('Quantas vezes você quer repetir? '))
for c in range(1, repeat +1):
    number = int(input(f'Número {c}: '))
    lista.append(number)
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
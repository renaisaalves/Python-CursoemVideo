#ex 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

#ALGORITMO
#1º pedir para o usuário informar vários números:
#   - o usuário insere um número e logo em seguida o programa pergunta se ele quer continuar inserindo; 
#   - o programa pedir para o usuário informar quantos números ele vai querer inserir. E, após o usuário inserir esses números, o programa perguntar se o usuário quer inserir mais números; 

lista = []
cont = 0

while resposta in 'SIMS':
    num = int(input('Digite um número: '))
    lista.append(num)
    resposta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()
    if resposta not in 'SIMS':
        break
print('=' * 30)
print(f'Sua lista completa: {lista}')
print(f'Lista em ordem alfabética: {lista.sort()}')
print(f'Lista em ordem decrescente: {lista.sort(reverse=True)}')
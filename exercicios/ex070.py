#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('~' * 30)
print('LOJA RA')
print('~' * 30)
print(' ')
while True:
    resposta = str(input('Quer continuar? ')).strip()
    if resposta in 'SimsimSIMsS':
        print('Testando')
    else:
        break
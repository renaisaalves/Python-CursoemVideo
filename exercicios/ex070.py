#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

contagem = total = 0 
print('=' * 45)
print('LOJÃO RA: CALCULE O GASTO DOS PRODUTOS AQUI!')
print('=' * 45)
while True:
    produto = str(input('Informe o nome do produto: ')).strip().upper()
    preço = float(input('Informe o preço do produto (R$): '))
    if preço > 1000: 
        contagem = contagem + 1 
    total = total + preço
    resposta = str(input('Quer continuar? ')).strip()
    if resposta in 'SimsimSIMsS':
        print('~' * 35)
    else:
        break
print('=' * 45)
print(f'O total gasto na compra foi: R${total:.2f}.')
print(f'Ao todo, {contagem} produtos custam mais de R$ 1000.')
print('=' * 45)

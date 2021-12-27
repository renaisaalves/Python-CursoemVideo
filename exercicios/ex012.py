#ex012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#FEITO POR MIM

preco = float(input('Qual é o preço do produto?\n R$:'))
novo = preco * 5 / 100
des = preco - novo
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}' .format(preco, des))


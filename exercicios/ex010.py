#ex010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
# 22/12/21 
# U$ 1.00 = R$ 5.69
# EURO$ = 1.00 = R$ 6.44

real = float(input('Quanto dinheiro você tem na carteira?\nR$:'))
dolar = real / 5.69
euro = real / 6.44
print('Com R${:.2f} você pode comprar U${:.2f} e EURO$ {:.2}' .format(real, dolar, euro))

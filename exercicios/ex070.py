#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

#FEITO POR MIM 

contagem = total = 0 
print('=' * 45)
print('LOJÃO RA: CALCULE O GASTO DOS PRODUTOS AQUI!')
print('=' * 45)
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço (R$): '))
    if preço > 1000: 
        contagem = contagem + 1 
    if total == 0: 
        produtobarato = produto 
        preçobarato = preço
    if preçobarato > preço:
        produtobarato = produto
        preçobarato = preço
    total = total + preço
    resposta = str(input('Quer continuar? ')).strip()
    if resposta in 'SimsimSIMsS':
        print('~' * 35)
    else:
        break
print('=' * 45)
print(f'O total gasto na compra foi: R${total:.2f}.')
print(f'Ao todo, {contagem} produtos custam mais de R$ 1000.')
print(f'O produto mais barato foi: {produtobarato} (R$ {preçobarato:.2f}).')
print('=' * 45)

#FEITO POR GUANABARA

total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço (R$): '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:^40}'.format('FIM DO PROGRAMA.'))
print(f'O total foi R${total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$ 1000.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

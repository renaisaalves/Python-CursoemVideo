#ex31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual é a distância da viagem? '))
preco200km = 0.50 * distancia 
if distancia <= 200:
    print('O preço da passagem para uma viagem de {}km é de: R${:.2f}.' .format(distancia, preco200km))
else:
    preco = 0.45 * distancia 
    print('O preço da passagem para uma viagem de {}km é de: R${:.2f}' .format(distancia, preco))
print('Tenha uma boa viagem!')
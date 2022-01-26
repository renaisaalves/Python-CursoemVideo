#ex055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
variavel = 0

for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: ' .format(c)))
    if peso - variavel > 0:
        maior = peso 
        variavel = peso 
    else:
        peso - variavel < 0
        menor = peso
        
print('O maior peso é {} e o menor peso é {}'. format(maior, menor))

# peso (50) - variavel (0) > 0: sim  (50 - 0 = 50)
# maior (50) = peso (50)
# variavel (50) = peso (50)

# peso (20) - variavel (50) < 0: sim (20 - 50 = -30)
# menor (0) = peso (20) 
# menor (20)

# peso (30) - variavel (50) < 0: sim (30 - 50 = -20)
# peso (30) < menor (20): 
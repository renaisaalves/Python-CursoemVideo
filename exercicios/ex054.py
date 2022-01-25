#ex054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
import datetime 

totalmenor = 0
totalmaior = 0

for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento ({}): ' .format(c)))
    if date.today().year - nasc < 18:
        totalmenor = totalmenor + 1
    else:
        date.today().year - nasc >= 18
        totalmaior = totalmaior + 1
print('Ao todo, {} pessoas são menores de idade e {} são maiores de idade.' .format(totalmenor, totalmaior))
 #ex043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
 
peso = float(input('Informe seu peso (KG): '))
altura = float(input('Informe sua altura: '))
IMC = peso / (altura ** 2)

if IMC < 18.5: 
    print('IMC ({}{:.1f}{}) = ABAIXO DO PESO!' .format('\033[1;35m', IMC, '\033[m'))
elif 18.5 <= IMC < 25:
    print('IMC ({}{:.1f}{}) = NORMAL{}' .format('\033[1;32m', IMC, '\033[m'))
elif 25 <= IMC < 30:
    print('IMC ({}{:.1f}{}) = ACIMA DO PESO' .format('\033[1;33m', IMC, '\033[m'))
elif 30 <= IMC < 40:
    print('IMC ({}{:.1f}{}) = OBESIDADE' .format('\033[1;31m', IMC, '\033[m'))
else: 
    IMC >= 40
    print('IMC ({}{:.1f}{}) = OBESIDADE MÓRBIDA' .format('\033[1;31m', IMC, '\033[m'))
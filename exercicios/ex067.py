#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

#FEITO POR MIM

print('=' * 20)
print('TABUADA EFICIENTE')
print('=' * 20)
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 20)
    if numero < 0:
        break 
    for contagem in range(0, 11):
        resultado = numero * contagem
        print(f'{numero} x {contagem} = {resultado}')
    print('=' * 20)
print('Fim do programa.')

#FEITO PELO GUANABARA


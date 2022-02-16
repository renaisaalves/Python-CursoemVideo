#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('=' * 20)
print('TABUADA EFICIENTE')
print('=' * 20)

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    for contagem in range(0, 11):
        resultado = numero * contagem
        print(f'{numero} x {contagem} = {resultado}')
print('Fim do programa.')
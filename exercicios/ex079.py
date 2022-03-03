#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
contador = 0
i = '\033[1;33m'
l = '\033[m'
while True:
    if contador == 0:
        valores.append(int(input('Digite um valor: ')))
        contador = contador + 1
    num = valores
    resposta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
    if resposta == 'S': 
        valores.append(int(input('Digite outro valor: ')))
        if num in valores:
            valores.remove(num)
    if resposta == 'N':
        break
print('=' * 30)
print(f'Valores informados: {i}{valores}{l}')
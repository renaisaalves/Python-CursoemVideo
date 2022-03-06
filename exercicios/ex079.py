#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
contador = 0
i = '\033[1;33m'
l = '\033[m'

print('=' * 30)

while True:
    if contador == 0:
        valores.append(int(input('Digite um valor: ')))
        contador += 1
    resposta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
    if resposta == 'S': 
        valores.append(int(input('Digite outro valor: ')))
    if resposta == 'N':
        valores.sort()
        if 4 in valores:
            valores.remove(4)
        break
print('=' * 30)
print(f'Valores informados: {i}{valores}{l}')
print('=' * 30)

#tem que receber um valor individual e analisar se esse número existe na lista

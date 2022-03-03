#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
contador = 0
while True:
    if contador == 0:
        valores.append(int(input('Digite um valor: ')))
        contador = contador + 1
    print('=' * 30)
    resposta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
    print('=' * 30)
    if resposta == 'S': 
        valores.append(int(input('Digite outro valor: ')))
    else:
        break
print(f'Valores informados: {valores}')

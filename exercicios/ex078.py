#ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#FEITO POR MIM 

valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite o {c}º valor: ')))
print(f'Valores digitados: {valores}')
valores.sort()
print(f'Menor valor: {valores[0]}')
print(f'Maior valor: {valores[4]}')
if valores[0] in valores:
    print(f'{valores[0]} foi encontrado nas posições {len([0])} ')

#1º passo: especifiquei o tipo da minha variável;
#2º passo: fiz um laço de repetição simples, do qual coleta 5 números do usuário;
#3º passo: todos os números informados entram dentro de uma lista;
#4º passo: faço o método de organizar os números [ordem crescente];
#5º passo: com a lista já organizada em ordem crescente, é só inserir a primeira posição [0] e a última [4]

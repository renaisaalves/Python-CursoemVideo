#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('==' * 8)
print('CALCULE A MÉDIA')
print('==' * 8)

contador = 0
resposta = ' '

valor = int(input('Digite um número: '))
contador = contador + 1 
m1 = valor
valor = int(input('Digite outro número: '))
contador = contador + 1 
m2 = valor
soma = m1 + m2 
media = soma / contador 
if m1 > m2:
    maior = m1 
    menor = m2 
else: 
    maior = m2 
    menor = m1 
print('TOTAL de números digitados: {}' .format(contador))
print('SOMA dos números: {}' .format(soma))
print('MÉDIA dos números: {:.2f}' .format(media))
print('MAIOR número: {}' .format(maior))
print('MENOR número: {}' .format(menor))

total = 0 
contador = int(input('Olá! Quantos números você deseja informar? '))
while total != contador: 
    total = total + 1 
    valor = int(input('Digite o {}º número: ' .format(total)))
    #resposta = str(input('Deseja inserir mais algum número? '))
print('TOTAL de números digitados: {}' .format(total))

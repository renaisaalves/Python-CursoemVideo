##65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0
resposta = 'SIM' or 'S'

print('==' * 8)
print('CALCULE A MÉDIA')
print('==' * 8)

contador = 0
resposta = 'SIMsSsim'
soma = media = 0

while resposta in 'SIMsSsim': 
    contador = contador + 1 
    if contador == 1: 
        numero = int(input('Digite um número: '))
        maior = menor = numero 
    numero = int(input('Digite outro número: '))
    if numero > maior:
        maior = numero
    else: 
        menor > numero
        menor = numero
    resposta = str(input('Quer continuar? '))
    if resposta in 'NãoNÃOnNnaoNAO':
        print('=' * 40)
        print('TOTAL de números digitados: {}' .format(contador))
        print('SOMA dos números: {}' .format(soma))
        print('MÉDIA dos números: {}' .format(media))
        print('MAIOR valor: {}' .format(maior))
        print('MENOR valor: {}' .format(menor))
        print('=' * 40)
print('Fim do programa')


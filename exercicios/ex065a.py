#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0
resposta = 'SIM' or 'S'

print('==' * 8)
print('CALCULE A MÉDIA')
print('==' * 8)

contador = 0
soma = 0
resposta = 'SIMsSsim'

while resposta in 'SIMsSsim':
    contador = contador + 1 
    numero = int(input('Digite um número: '))
    if contador == 1: 
        maior = menor = numero
    if numero > maior:
        maior = numero
    else: 
        numero < menor
        menor = numero
    soma = soma + numero
    media = soma / contador
    resposta = str(input('Quer continuar? '))
    if resposta in 'NãoNÃOnNnaoNAO':
        print('=' * 40)
        print('TOTAL de números digitados: {}' .format(contador))
        print('SOMA dos números: {}' .format(soma))
        print('MÉDIA dos números: {:.2f}' .format(media))
        print('MAIOR valor: {}' .format(maior))
        print('MENOR valor: {}' .format(menor))
        print('=' * 40)
print('Fim do programa')
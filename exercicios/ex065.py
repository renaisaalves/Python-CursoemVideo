##65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('==' * 8)
print('CALCULE A MÉDIA')
print('==' * 8)

contador = 0
resposta = 'SIMsSsim'

while resposta in 'SIMsSsim': 
    numero = int(input('Digite outro número: '))
    contador = contador + 1 
    resposta = str(input('Quer continuar? '))
    if resposta != 'SIMsSsim' and 'NãoNÃOnNnaoNAO':
        resposta = print('Resposta inválida. Digite [sim/não]: ')
    if resposta in 'NãoNÃOnNnaoNAO':
        print('TOTAL de números digitados: {}' .format(contador))
        print('SOMA dos números: {}' .format(soma))
        print('MÉDIA dos números: {}' .format(media))
        print('MAIOR valor: {}' .format(maior))
        print('MENOR valor: {}' .format(menor))
print('Fim do programa')

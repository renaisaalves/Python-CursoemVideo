#ex68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint 

PAR = 'PAR' or 'P'
IMPAR = 'IMPAR' or 'I'
vitoria = 0
while True: 
    jogador = int(input('Escolha um número [0/5]: '))
    escolha = str(input('PAR ou IMPAR? ')).upper()
    computador = randint(0, 5)
    if escolha == PAR:
        escolhapc = IMPAR
    else:
        escolhapc = PAR
    soma = jogador + computador 
    if soma % 2 == 0:
        resultado = PAR 
    else: 
        resultado = IMPAR 
    if escolha == resultado:
        print('Você ganhou!')
        vitoria = vitoria + 1 
    else:
        print('Você perdeu!')
        break
print(f'Você escolheu {escolha} e o computador escolheu {escolhapc}.')
print(f'A soma entre {jogador} + {computador} = {soma}, resultando em {resultado}!')
print(f'Você teve {vitoria} vitórias.')
    
        

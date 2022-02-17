#ex68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint 

PAR = 'PAR' or 'P'
IMPAR = 'IMPAR' or 'I'
vitoria = 0
while True: 
    jogador = int(input('Escolha um número [0/5]: '))
    escolha = str(input('PAR ou IMPAR? ')).upper()
    computador = randint(0, 5)
    if jogador == PAR:
        computador == IMPAR
    else:
        jogador == IMPAR
        computador == PAR
    soma = jogador + computador 
    if soma % 2 == 0:
        soma == PAR 
    else: 
        soma == IMPAR 
    if soma and jogador == PAR:
        print('Você ganhou!')
        vitoria = vitoria + 1 
    else:
        print('Você perdeu!')
        break
    
        

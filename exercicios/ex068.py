#ex68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint 

PAR = 'PAR'
IMPAR = 'IMPAR'
vitoria = 0

while True:
    jogador = int(input('Escolha um número [0/10]: '))
    numjogador = str(input('PAR ou IMPAR? ')).upper()
    computador = randint(0, 10)
    if numjogador == PAR: 
        numcomputador = IMPAR
    else:
        numcomputador = PAR 
    soma = jogador + computador 
    if soma % 2 == 0:
        resultado = PAR 
    else:
        resultado = IMPAR
    if resultado == numjogador:
        print('VOCÊ VENCEU!')
        vitoria = vitoria + 1
    else: 
        print('VOCÊ PERDEU!')
        break
print(f'Você escolheu {escolhajogador} e o computador escolheu {escolhapc}.')
print(f'A soma entre {jogador} + {computador} = {soma}, resultando em {resultado}!')
print(f'Você teve {vitoria} vitórias.')
    
        

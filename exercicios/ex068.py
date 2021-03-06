#ex68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint 

#FEITO POR MIM 

print('=' * 20)
print('JOGO DO PAR E ÍMPAR!')
print('=' * 20)

PAR = 'PAR'
IMPAR = 'IMPAR'
vitoria = 0

while True:
    jogador = int(input('Escolha um número [0/10]: '))
    while jogador < 0 or jogador > 10:
        jogador = int(input('Número inválido. Escolha outro número [0/10]: '))
    numjogador = str(input('PAR ou IMPAR? ')).upper().strip()
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
        print('~=' * 20)
        print(f'DEU {resultado}! VOCÊ VENCEU!')
        print('~=' * 20)
        vitoria = vitoria + 1
        print(f'Você escolheu {numjogador} e o computador escolheu {numcomputador}.')
        print(f'A soma entre {jogador} + {computador} = {soma}, {soma} é um número {resultado}!')
        print(f'Essa foi a sua {vitoria}ª vitória!')
        print(' ')
    else: 
        print('-=' * 20)
        print(f'DEU {resultado}! O COMPUTADOR VENCEU!')
        print('-=' * 20)
        break
print(f'Você escolheu {numjogador} e o computador escolheu {numcomputador}.')
print(f'A soma entre {jogador} + {computador} = {soma}, {soma} é um número {resultado}!')
print(f'No total, você teve {vitoria} vitória(s).')
    
#FEITO PELO GUANABARA

v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v = v + 1 
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v = v + 1 
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

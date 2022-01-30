#ex028: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#FEITO POR MIM / VERSÃO COM COR 

from random import randint
print('=' * 30)
print('REMAKE DO JOGO DO DESAFIO 28!')
print('=' * 30)
tentativas = 1
computador = randint(0, 3)
jogador = int(input('Digite um número [0/3]: '))
while jogador != computador:
    tentativas = tentativas + 1
    jogador = int(input('{}ERROU!{}\nDigite outro número [0/3]: ' .format('\033[1;31m', '\033[m')))
if tentativas == 1:
    jogador == computador
    print('{}PARABÉNS!{} Você acertou na primeira tentativa!' .format('\033[1;32m', '\033[m'))
else: 
    jogador == computador and tentativas > 1
    print('{}ACERTOU!{}' .format('\033[1;32m', '\033[m'))
    print('Foram necessárias {}{}{} tentativas para você acertar.' .format('\033[1;31m', tentativas, '\033[m'))


#ex72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

#MINHA RESOLUÇÃO 

while True:
    numero = int(input('Digite um número: '))
    while numero < 0 or numero > 20:
        numero = int(input('Número inválido. Digite outro [0/20]: '))
    print('Você digitou o número',tupla[numero])
    resposta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
    if resposta == 'N':
        break
    
#RESOLUÇÃO GUANABARA

while True:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {tupla[numero]}')
#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('=~' * 8)
print('CALCULE A MÉDIA')
print('=~' * 8)

contador = 0

numero = int(input('Digite um número: '))
armazém = numero
contador = 1
while not 'SIM':
    numero = int(input('Digite um número: '))
    transferidor = numero
    acumulador = transferidor + armazém
    armazém = acumulador
    contador = contador + 1
    if contador == 2:
        resposta = str(input('Você quer continuar a digitar os valores? [SIM/NÃO]: ')).upper().strip()
    media = armazém / contador
    print('A média entre todos os valores informados foi {:.2f}.' .format(media))
    print('Dentre os números informados, o menor foi {} e o maior foi {}.' .format())
print('FIM DO PROGRAMA.')
    

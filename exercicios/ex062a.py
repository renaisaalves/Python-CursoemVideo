#62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

#FEITO POR MIM

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = 0
while termo < 10:
    termo = termo + 1
    an = a1 + (termo - 1) * r
    print(an, '➝ ', end=' ')
    if termo == 10:
        print('PAUSA')
        novotermo = int(input('\nQuantos termos você quer mostrar a mais? '))
        if novotermo != 0:
            termo = novotermo + termo
            print('')
        else:
            novotermo == 0
print('FIM DO PROGRAMA.')
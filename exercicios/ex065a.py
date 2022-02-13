#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('==' * 8)
print('CALCULE A MÉDIA')
print('==' * 8)

contador = 0 
resposta = 'NULO'
while contador != 2: 
    contador = contador + 1
    n = int(input('Digite um número: '))
    if contador == 1:
        m1 = n
    if contador == 2:
        m2 = n
        if m1 > m2:
            maior = m1 
            menor = m2
        else:
            m2 > m1
            maior = m2
            menor = m1
            soma = maior + menor
            media = soma / 2
        resposta = str(input('Você quer digitar mais algum número? [SIM/NÃO]: ')).strip()    
        while resposta in 'SIMsimSs':
            n = int(input('Digite mais um número: '))
            contador = contador + 1
            if n > maior:
                maior = n
            if n < menor:
                menor = n
            soma = maior + menor 
            media = soma / contador
            resposta = str(input('Você quer digitar mais algum número? [SIM/NÃO]: ')).strip()
        else: 
            print('=' * 40)
            print('A MÉDIA entre os {} valores informados foi {:.2f}' .format(contador, media))
            print('=' * 40)
            print('O MAIOR valor é {} e o MENOR valor é {}' .format(maior, menor))
            print('=' * 40)
print('FIM DO PROGRAMA.')
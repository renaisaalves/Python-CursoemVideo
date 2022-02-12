#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('=~' * 8)
print('CALCULE A MÉDIA')
print('=~' * 8)

contador = 0 

while contador != 2: 
    contador = contador + 1
    n = int(input('Digite um número: '))
    if contador == 1:
        m1 = n
    if contador == 2:
        m2 = n
        resposta = str(input('Você quer digitar mais algum número? [SIM/NÃO]: ')).strip()
        if resposta in 'SIMsimsS':
            while resposta in 'SIMsimS':
                n = int(input('Digite mais um número: '))
        else: 
            if m1 > m2:
                maior = m1 
                menor = m2
            else:
                maior = m2
                menor = m1
            soma = m1 + m2 
            media = soma / 2
            print('=' * 40)
            print('A MÉDIA entre os dois valores informados foi {:.2f}' .format(media))
            print('=' * 40)
            print('O MAIOR valor é {} e o MENOR valor é {}' .format(maior, menor))
            print('=' * 40)
            
#Para que a média aconteça, é necessário, no mínimo, de dois números para serem somados e divididos. 
#A minha ideia inicial é que o usuário digite dois números e o programa já deixe pronto todas as informações que ele precisa (média e qual foi o menor e maior número informado.)
#Se o usuário quiser continuar informando mais valores (acima de 2), vou adicionar uma estrutura de repetição que faça a mesma pergunta a cada valor digitado, pois é imprevisível saber quantos números o usuário quer. 
#A soma possui a seguinte estrutura: soma = n1 + n2 
#A média possui a seguinte estrutura: media = soma / contador (O contador vai fazer a contagem dos elementos informados)
#A comparação de < e > possui a seguinte estrutura: a primeira repetição vai armazenar o primeiro valor e a segunda repetição vai comparar o novo valor com o valor anterior. A partir disso, tudo estará pronto para ser exercido no próximo while.
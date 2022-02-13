#65: Crie um programa que leia vários números inteiros pelo teclado. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 

print('=' * 15)
print('CALCULE A MÉDIA')
print('=' * 15)

contador = 2

valor = int(input('Digite um valor: '))
m1 = valor 
valor = int(input('Digite outro valor: '))
m2 = valor 
resposta = str(input('Você quer digitar mais algum valor? [Sim/Não]: ')).strip()
while resposta in 'SIMsimSimsS':
    resposta = True 
    valor = int(input('Digite mais um valor: '))
    contador = contador + 1
    resposta = str(input('Você quer digitar mais algum valor? [Sim/Não]: ')).strip()
print('{}' .format(contador))
print('Fim do programa.')

#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#Seu programa deverá realizar a operação solicitada em cada caso.

#FEITO POR MIM

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
programa = False
while not programa:
    print('''[ 1 ] SOMAR 
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR 
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Escolha uma opção: '))
    while opcao > 5:
        opcao = int(input('Opção inválida. Digite outro número: '))
    if opcao == 1:
        resultado = valor1 + valor2
        print('=' * 30)
        print('A SOMA de {} + {} = {}' .format(valor1, valor2, resultado))
        print('=' * 30)
    elif opcao == 2:
        resultado = valor1 * valor2
        print('=' * 30)
        print('A MULTIPLICAÇÃO de {} * {} = {}' .format(valor1, valor2, resultado))
        print('=' * 30)
    elif opcao == 3:
        if valor1 == valor2: 
            print('=' * 30)
            print('{} == {} (são iguais)' .format(valor1, valor2))
            print('=' * 30)
        elif valor1 > valor2:
            print('=' * 30)
            print('{} > {}' .format(valor1, valor2))
            print('=' * 30)
        else:
            print('=' * 30)
            print('{} > {}' .format(valor2, valor1))
            print('=' * 30)
    elif opcao == 4: 
        print('*' * 30)
        valor1 = int(input('Primeiro novo valor: '))
        valor2 = int(input('Segundo novo valor: '))
        print('*' * 30)
    else:
        opcao == 5
        programa = True
print('FIM DO PROGRAMA.')
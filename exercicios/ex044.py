#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

valor = float(input('Informe o valor do produto (R$): '))
escolha = int(input('''Qual a forma de pagamento? 
1 = À VISTA/CHEQUE
2 = À VISTA NO CARTÃO (5% de desconto)
3 = PARCELAMENTO NO CARTÃO (em até 2x)
4 = PARCELAMENTO NO CARTÃO (em 3x ou mais)
Digite a opção aqui: '''))

if escolha == 1: 
    desconto = (valor * 10) / 100
    pagamento = valor - desconto
    print('OPÇÃO ESCOLHIDA: 1 (dinheiro/cheque)')
    print('O pagamento à vista em dinheiro ou cheque oferece um desconto de 10% do total da compra!')
    print('Valor original: {}R${:.2f}{}' .format('\033[1;37m', valor, '\033[m'))
    print('Valor com desconto de 10%: {}R${:.2f}{}.\nBoas compras!' .format('\033[1;32m', pagamento, '\033[m'))
elif escolha == 2:
    desconto = (valor * 5) / 100
    pagamento = valor - desconto
    print('OPÇÃO ESCOLHIDA: 2 (à vista no cartão)')
    print('O pagamento à vista no cartão oferece um desconto de 5% do total da compra!')
    print('Valor original: {}R${:.2f}{}' .format('\033[1;37m', valor, '\033[m'))
    print('Valor com desconto de 10%: {}R${:.2f}{}.\nBoas compras!' .format('\033[1;32m', pagamento, '\033[m'))
elif escolha == 3:
    pagamento = valor / 2
    print('OPÇÃO ESCOLHIDA: 3 (em até 2x no cartão)')
    print('Valor original: {}R${:.2f}{}' .format('\033[1;37m', valor, '\033[m'))
    print('Valor parcelado em 2x: {}R${:.2f}{}.\nBoas compras!' .format('\033[1;32m', pagamento, '\033[m'))
elif escolha == 4:
    parcelas = int(input('Em quantas parcelas? '))
    parcela = valor / parcelas
    juros = (parcela * 20) / 100 
    pagamento = parcela + juros
    total = pagamento * parcelas
    print('OPÇÃO ESCOLHIDA: 4 (3x ou mais no cartão)')
    print('Ao parcelar em 3x ou mais vezes, haverá um acréscimo de juros em {}20%{}.' .format('\033[1;31m', '\033[m'))
    print('Quantidade de parcelas selecionadas: {}{}{}' .format('\033[1;37m', parcelas, '\033[m'))
    print('Valor original: {}R${:.2f}{}' .format('\033[1;37m', valor, '\033[m'))
    print('Valor parcelado com juros de 20%: {}R${:.2f}{}' .format('\033[1;31m', pagamento, '\033[m'))
    print('Valor final do produto: {}R${}{}.\nBoas compras!' .format('\033[1;37m', total, '\033[m'))
else: 
    escolha != 1 or escolha != 2 or escolha != 3 or escolha != 4
    print('Opção inválida.')
    

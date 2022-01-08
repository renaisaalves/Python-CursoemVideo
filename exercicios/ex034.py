#ex034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Olá! Informe o seu salário: R$'))

if salario > 1250:
    aumento = (salario * 10 / 100) + salario
    print('O seu salário com o aumento de 10% será de: R$ {:.2f}.' .format(aumento))
else:
    salario <= 1250
    aumento = (salario * 15 / 100) + salario
    print('O seu salário com o aumento de 15% será de: R$ {:.2f}.' .format(aumento))
    
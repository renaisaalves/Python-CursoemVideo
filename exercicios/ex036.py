#ex036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Informe seu salário (R$): '))
anos = int(input('Em quantas anos você deseja pagar? '))
meses = anos * 12
parcelas = valorcasa / meses

if parcelas < 30 * salario / 100:
    print('O seu empréstimo de R${:.2f} em {} anos foi \033[1;32mautorizado\033[m.' .format(parcelas, anos))
elif parcelas > 30 * salario / 100: 
    print('O empréstimo de R${:.2f} em {} anos foi \033[1;31mnegado\033[m.' .format(parcelas, anos))
    
    # 100.000 / 3.500 / quero pagar em 5 anos / 5 * 12 = 60 meses
    # dentro desses 60 meses, eu preciso pagar X ao mês. Esse X é a minha parcela. 
    # se a parcela > 30 % do meu salário, o empréstimo será negado.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
p = n1 * n2 
print('O produto entre {} e {} é igual a {}' .format(n1, n2, p))

sal = float(input('Digite o valor do salário: '))
per = int(input('Digite o percentual de aumento: '))
value = sal * per
value1 = value / 100
newsal = value1 + sal
print('O novo valor do seu salário, baseado na porcentagem é de {}' .format(newsal))

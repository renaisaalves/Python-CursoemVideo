#AULA15 - BREAK (PARE)

n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma vale {s}')

nome = 'Rayssa'
idade = '22'
salario = 3000.00
print(f'A {nome} tem {idade} anos e o seu salário é de {salario:.2f}.')

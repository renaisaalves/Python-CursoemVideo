#Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal (salário semanal) tendo em conta as horas extraordinárias. O salário é calculado do seguinte modo: se o número de horas for menor que 40, então o salário é dado pelo produto do número de horas pelo salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar. 

print('=' * 30)
print(f'{"CÁLCULO SALARIAL":^30}')
print('=' * 30)

salario_hora = float(input('Salário (hora): '))
horas_dia = int(input('Horas trabalhas (dia): '))
salario_dia = salario_hora * horas_dia
if horas_dia > 8:
    horas_extras = horas_dia - 8
print(f'Salário por hora: EURO$ {salario_hora}')
print(f'Horas trabalhadas ao dia: {horas_dia}')
print(f'Horas extraordinárias acumuladas na semana: {horas_extras}')

for dia in range(1, 8):
    print('Dia {dia}º')
    salario_hora.append(float(input('Salário (hora): ')))
    horas_dia = int(input('Horas trabalhas (dia): '))
    salario_dia = salario_hora * horas_dia
    if horas_dia > 8:
        horas_extras = horas_dia - 8
    
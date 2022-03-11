#Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal (salário semanal) tendo em conta as horas extraordinárias. O salário é calculado do seguinte modo: se o número de horas for menor que 40, então o salário é dado pelo produto do número de horas pelo salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar. 

horas_extras_totais = salario_semanal = []

print('=' * 30)
print(f'{"CÁLCULO SALARIAL":^30}')
print('=' * 30)

salario_hora = float(input('Salário (hora): '))
for c in range(1, 8):
    horas_dia = int(input(f'Horas trabalhas ({c}º dia): '))
    salario_dia = salario_hora * horas_dia
    salario_semanal.append(salario_dia)
    salario_semanal += sum(salario_semanal)
    if horas_dia > 8:
        horas_extras = horas_dia - 8
        horas_extras_totais.append(horas_extras)
        horas_extras_acumuladas = sum(horas_extras_totais)
print('-' * 30)
print(f'Salário semanal: EURO$ {salario_semanal}')
print(f'Total de horas trabalhadas na semana: {horas_dia}h')
print(f'Horas extraordinárias acumuladas na semana: {horas_extras_acumuladas}h')

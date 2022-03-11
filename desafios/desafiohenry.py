#Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal (salário semanal) tendo em conta as horas extraordinárias. O salário é calculado do seguinte modo: se o número de horas for menor que 40, então o salário é dado pelo produto do número de horas pelo salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar. 

salario_semanal = horario_semanal = horas_extras = salario_extra = dias_trabalhados = 0

print('=' * 30)
print(f'{"CÁLCULO SALARIAL":^30}')
print('=' * 30)

salario_hora = float(input('Salário por hora (¢EUR): '))
print('=' * 30)
for c in range(1, 8):
    horas_dia = int(input(f'Horas trabalhadas ({c}º dia): ')) 
    horario_semanal = horario_semanal + horas_dia
    if horas_dia > 0:
        dias_trabalhados = dias_trabalhados + 1
    if horario_semanal < 40:
        salario_semanal = horario_semanal * salario_hora
    if horario_semanal > 40:
        horas_extras = horario_semanal - 40
        salario_extra = horas_extras * salario_hora
        salario_semanal= salario_semanal + salario_extra
print('=' * 30)
print(f'Salário semanal: ¢EUR {salario_semanal:.2f} por dias trabalhados')
print(f'Total de horas trabalhadas na semana: {horario_semanal}h')
print(f'Total de dias trabalhados: {dias_trabalhados}')
print(f'Total de horas-extras: {horas_extras}h')
print(f'Salário-extra semanal: ¢EUR {salario_extra}')
print('=' * 30)
#salário_hora (fixo) = definido pelo usuário
#horário_semanal (definido pelo exercício) = 40h 

#TIRANDO COMO PARÂMETRO MEU IRMÃO
#R$224 = 40h 
#R$ 





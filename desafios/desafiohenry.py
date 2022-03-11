#Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal (salário semanal) tendo em conta as horas extraordinárias. O salário é calculado do seguinte modo: se o número de horas for menor que 40, então o salário é dado pelo produto do número de horas pelo salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar. 

salario_semanal = 0

print('=' * 30)
print(f'{"CÁLCULO SALARIAL":^30}')
print('=' * 30)

salario_hora = float(input('Salário (hora): '))
print('=' * 30)
for c in range(1, 8):
    horas_dia = int(input(f'Horas trabalhas ({c}º dia): '))
        
print('=' * 30)
print(f'Salário semanal: {salario_semanal}')

#1º Vou considerar o salário_hora como fixo (não altera o seu valor).
#2º Vou considerar que não há uma jornada de horário-fixo (como a tradicional CLT brasileira). Desse modo, o usuário pode decidir a sua própria jornada de trabalho. Isso significa, então, que sempre precisaremos perguntar ao usuário quantas horas ele trabalhou no dia. Para facilitar o algoritmo, vou usar o laço de repetição for (uma semana corresponde à 7 dias, logo, temos um tempo [range] definido), que vai automaticamente coletar os horários trabalhados do usuário por dia. 
#3º Durante a coleta de dados (horas trabalhadas no dia), vou precisar "armazenar" esses horários em algum lugar. Inicialmente, eu pensei em guardar os valores dentro de uma lista, mas como não domino a função, achei melhor continuar fazendo no modo tradicional, ao menos até garantir que o código esteja 100% funcional. 



#ex089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aluno = []
cadastro = list()

print('-'* 40)
print(f'{"BOLETIM ESCOLAR":^40}')
print('-'* 40)
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    cadastro.append(aluno[:])
    aluno.clear()
    resposta = str(input('Quer continuar? ')).upper()
    if resposta not in 'SIMS':
        for a in cadastro:
            media = (a[1] + a[2]) / 2
            a.append(media)
        break
print(cadastro)
print('=' * 40)
print(f'{"Nº"}{"NOME":^32}{"MÉDIA"}')
print('=' * 40)
for p, i in enumerate(cadastro):
    print(p, f'{i[0]:^32}', i[3])
print('-' * 40)
print(f'{"CONSULTA INDIVIDUAL":^40}\nVocê pode acessar as notas individualmente. Para sair, digite 999.')
print('-' * 40)
while True:
    num = int(input('Mostrar notas de qual aluno?\nNº: '))
    if cadastro[num]:
        print(f'As notas de {cadastro[num][0]} são: {cadastro[num][1]} e {cadastro[num][2]}.')
    if num == 999:
        break

#a = aluno
#p = posição
#i = valor
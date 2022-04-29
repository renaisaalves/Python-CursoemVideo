#ex089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aluno = []
cadastro = list()

print('='* 40)
print(f'{"BOLETIM ESCOLAR":^40}')
print('='* 40)
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
        for aluno in cadastro:
            media = (aluno[1] + aluno[2]) / 2
            aluno.append(media)
        break
print(cadastro)
print('=' * 40)
print(f'{"Nº"}{"NOME":^32}{"MÉDIA"}')
print('-' * 40)
for c, i in enumerate(cadastro):
    print(c, i[0], i[3])
print('=' * 40)

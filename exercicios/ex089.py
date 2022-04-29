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
    print('-' * 20)
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    cadastro.append(aluno[:])
    aluno.clear()
    resposta = str(input('Quer continuar? ')).upper()
    print('-' * 20)
    if resposta not in 'SIMS':
        for c in cadastro:
            media = (c[1] + c[2]) / 2
            print(media)
        break
print(cadastro)
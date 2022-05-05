#ex090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Nome: ')).capitalize()
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media > 5:
    situação = 'Aprovado'
else:
    situação = 'Reprovado'
dicionario = {'aluno': nome, 'media': media, 'situação': situação}
print(dicionario)
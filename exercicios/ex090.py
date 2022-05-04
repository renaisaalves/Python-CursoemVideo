#ex090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Nome: ')).capitalize()
media = float(input('Média: '))
dicionario = {'nome': nome, 'media': media}
print(dicionario)
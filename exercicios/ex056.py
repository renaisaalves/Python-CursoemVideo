#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

#FEITO PELO GUANABARA / NÃO CONSEGUI FAZER

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
idademulher = 0
totmulher = 20

for p in range(1, 5):
    print('==== {}ª pessoa ====' .format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Gênero: ')).strip().upper()
    somaidade = somaidade + idade
    mediaidade = somaidade / p
    if p == 1 and sexo == 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        idademulher = idade < 20
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher = totmulher + 1
print('A média da idade do grupo é de {} anos' .format(mediaidade))
print('O nome do homem mais velho é {} e ele tem {} anos.' .format(nomevelho, maioridadehomem))
print('{} mulheres tem menos de 20 anos.' .format(totmulher))
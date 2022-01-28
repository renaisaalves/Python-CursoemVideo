#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

#FEITO PELO GUANABARA / NÃO CONSEGUI FAZER

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('==== {}ª pessoa ====' .format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Gênero: ')).strip().upper()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print('A média da idade do grupo é de {} anos' .format(mediaidade))
print('O nome do homem mais velho é {} e ele tem {} anos.' .format(nomevelho, maioridadehomem))
print('Ao todo, são {} mulheres com menos de 20 anos.' .format(totmulher20))
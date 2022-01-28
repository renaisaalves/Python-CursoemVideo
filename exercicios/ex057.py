#ex057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe  seu sexo [M/F]: ')).strip().upper() [0] #[0] significa pegar somente a primeira letra
while sexo not in 'MmFf':
    str(input('Dados inválidos. Por favor, informe novamente [M/F]: ')).strip().upper() [0]
print('Sexo {} registrado com sucesso.' .format(sexo))
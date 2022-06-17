#ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas; a maior nota; a menor nota; a média da turma; a situação (opcional)

def notas(*valores):
    quant = 1
    while True:
        if quant == 1:
            maior = menor = valores
        quant += 1
        if quant > 1:
            if valores > maior:
                maior = valores
            if valores < menor:
                menor = valores
        if quant == resp:
            break
resp = notas(5.5, 8, 1.5)
print(resp)
#{'quantidade de notas': quant, 'maior nota': maior, 'menor nota': menor}
# sit=True
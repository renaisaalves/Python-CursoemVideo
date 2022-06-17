#ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas; a maior nota; a menor nota; a média da turma; a situação (opcional)

def notas(*valores):
    quant = len(valores)
    media = (sum(valores)) / quant
    a = 0
    for c in valores:
        if a == 0:
            maior = menor = c
            a += 1
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    boletim = {'quantidade de notas': quant, 'maior nota': maior, 'menor nota': menor, 'média': media}
    return boletim
resp = notas(1, 3.6, 9.8, 5.5, 6, 4.7)
print(resp)
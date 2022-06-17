#ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas; a maior nota; a menor nota; a média da turma; a situação (opcional)

def notas(*valores):
    quant = len(valores)
    dados = list(valores)
    for c, i in dados:
        if c == 0:
            maior = menor = i
        if c > 0:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
    boletim = {'quantidade de notas': quant, 'maior nota': maior, 'menor nota': menor}
    return boletim
resp = notas(5.5, 8, 1.5)
print(resp)
# sit=True
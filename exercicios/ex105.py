#ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas; a maior nota; a menor nota; a média da turma; a situação (opcional)

def notas(*valores):
    quant = len(valores)
    for c in range(quant):
        if c == 0:
            maior = menor = valores[0]
        if c > 0:
            if c > maior:
                maior = valores
            if c < menor:
                menor = valores
    valores = {'quantidade de notas': quant, 'maior nota': maior, 'menor nota': menor}
    return valores
resp = notas(5.5, 8, 1.5)
print(resp)
# sit=True
#ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas; a maior nota; a menor nota; a média da turma; a situação (opcional)

def notas(*valores):
    quant = len(valores)
    media = (sum(valores)) / quant
    boletim = {'quantidade de notas': quant, 'média': media}
    return boletim
resp = notas(5.5, 8, 1.5)
print(resp) 
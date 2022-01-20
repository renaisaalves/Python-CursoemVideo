#AULA13: ESTRUTURA DE CONTROLE DE REPETIÇÃO
from re import S


for c in range(0, 6):
    print('Olá, Mundo!')
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 4):
    n = int(input('Digite um valor: '))
print('FIM')

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = 0
    s = s + n
print('O somatório de todos os valores foi {}.' .format(s))
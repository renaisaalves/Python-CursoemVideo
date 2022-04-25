#ex087: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

a = '\033[1;33m'
r = '\033[1;36m'
v = '\033[1;32m'
f = '\033[m'

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)

print('MATRIZ criada a partir dos valores digitados:\n')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() 
print(f'\nA soma de todos os valores {a}pares{f} foi: {a}amor{f}')
print(f'A soma dos valores da terceira coluna foi: {r}paz{f}')
print(f'O maior valor da segunda linha foi: {v}esperança{f}')
print('-=' * 30)


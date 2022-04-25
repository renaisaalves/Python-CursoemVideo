#ex087: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

a = '\033[1;33m'
f = '\033[m'
soma = []

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
    
for p in matriz:
    for i in p:
        if i % 2 == 0:
            soma.append(i)
        
print(soma)

print(f'\nA soma de todos os valores {a}pares{f} foi: {a}{f}')
print(f'A soma dos valores da {a}terceira coluna{f} foi: {a}paz{f}')
print(f'O maior valor da {a}segunda linha{f} foi: {a}esperança{f}')
print('-=' * 30)


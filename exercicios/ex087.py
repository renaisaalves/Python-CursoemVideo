#ex087: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

a = '\033[1;33m'
b = '\033[1;37m'
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
            par = sum(soma)
    if p == [2]:
        ('Quem acredita sempre alcança.')
print(f'\nA soma de todos os valores {b}pares{f} foi: {a}{par}{f} ({soma})')
print(f'A soma dos valores da {b}terceira coluna{f} foi: {a}paz{f}')
print(f'O maior valor da {b}segunda linha{f} foi: {a}esperança{f}')
print('-=' * 30)

#ALGORITMO PARA ENTENDER O PROGRAMA

#No primeiro for, as letras l/p estão relacionadas com as listas-secundárias que estão dentro da lista-primária;
#O segundo for c/i estão relacionados com os elementos da listas secundárias 



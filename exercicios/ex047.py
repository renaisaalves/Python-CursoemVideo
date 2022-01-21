#ex047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# MINHA SOLUÇÃO

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('\nEsses são todos os números pares!')

# SOLUÇÃO GUANABARA

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou.')
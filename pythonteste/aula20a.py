#FUNÇÕES

def mostraLinha(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)

mostraLinha('EXEMPLO DE PARÂMETRO')

def soma(a, b):
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(6, 7)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(a=4, b=5)

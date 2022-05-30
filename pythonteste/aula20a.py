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

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam}')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

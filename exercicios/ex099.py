#ex099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(m):
    print('*' * 30)
    for c, i in enumerate(m):
        if c == 0:
            mai = men = i
        else:
            if i > mai:
                mai = i
            if i < men:
                men = i
    print(f'O maior valor é {mai} e o menor é {men}')
    print('*' * 30)
values = list()
while True:
    values.append(int(input('Número: ')))
    resp = str(input('Deseja inserir outro número? [S/N]: ')).upper()[0]
    if resp in 'N':
        break
maior(values)

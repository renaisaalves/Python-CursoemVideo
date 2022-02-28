#ex077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#NÃO CONSEGUI FAZER
a = '\033[1;33m'
v = '\033[1;32m'
l = '\033[m'
palavras = ('abacaxi', 'tomate', 'uva', 'morango', 'melancia', 'coco', 'cenoura', 'mirtilo')

for p in palavras:
    print(f'\nNa palavra {a}{p}{l} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{v}{letra}{l}', end='')

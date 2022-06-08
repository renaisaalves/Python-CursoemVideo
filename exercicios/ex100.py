#ex100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
def sorteia():
    sorteio = list()
    for c in range(0, 5):
        sorteio.append(randint(0, 100))
    print(f'Números sorteados: {sorteio}')
    
def somaPar():
    pares = list()
    for c, v in sorteia():
        if v % 2 == 0:
            pares.append(c)
            soma = sum(pares)
    print(f'Os números pares são: {pares}')
    print(f'A soma entre os números pares foram: {soma}')
sorteia()
somaPar()
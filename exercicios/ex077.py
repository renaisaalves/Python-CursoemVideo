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
            
#PASSO A PASSO PARA ENTENDER A RESOLUÇÃO

#1º Criei uma tupla com várias palavras.
#2º A tupla 'palavras' possui 8 termos: 'abacaxi' = 1º termo/posição 0 na memória e assim em diante.
#3º Fiz um laço de repetição. 'p' vai girar cada termo da dupla 'palavras', até acabar, ex: abacaxi, tomate etc.
#4º Vamos traduzir o 1º comando: 'Na palavra abacaxi (1º termo/posição 0 na memória) temos:'
#5º Delimitei para a repetição continuar em cada termo (p). 
#6º Temos outro laço. Enquanto 'letra' (cada palavra) in 'p' (termo = 'abacaxi', 'tomate', etc.)
#7º Se 'letra' (cada palavra) tiver 'a e i o u', escreva essas vogais. 
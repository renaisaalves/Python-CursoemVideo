#ex042: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 == r2 == r3:
    print('Os segmentos acima PODEM formar um triângulo EQUILÁTERO!')
elif r1 == r2 > r3 or r1 == r3 > r2 or r2 == r3 > r1:
    print('Os segmentos acima PODEM formar um triângulo ISÓCELES!')
else:
    print('Os segimentos acima NÃO PODEM formar um triângulo!')
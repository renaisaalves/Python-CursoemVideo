#AULA16 = TUPLAS ()
lanche = ('bolo', 'pastel', 'pizza', 'refrigerante', 'coxinha', 'brigadeiro')
print(lanche) #exibe todas os elementos da tupla
print(lanche[0:3]) #começa na posição 0 [bolo] e vai até a posição 2 [pizza]
print(lanche[3]) #exibe a posição 3 [refrigerante]
print(lanche[-2]) #conta da direita para a esquerda [coxinha -2, brigadeiro -1]
print(len(lanche)) #mostra quantas posições existem na variável [6]
print(sorted(lanche)) #se for números, em ordem crescente; se for letras, em ordem alfabética

for c in lanche:
    print(f'Eu vou comer {c}.')

for pos, comida in enumerate(lanche): #enumerate vai me dar a possibilidade de numerar as posições e seus nomes
    print(f'Eu vou comer {comida} na posição {pos}.')
    
#Também dá pra fazer dessa forma:
#for cont in range(0, len(lanch):
#    print(lanche[cont] ou f'Eu vou comer {lanche[cont]} na posição {cont}')

a = (2, 5, 7)
b = (5, 8, 1, 2)
c = a + b #vai juntar a tuplas a e b 
print(c)
print(len(c))
print(c.count(5)) #quantas vezes está aparecendo o número 5 dentro de c
print(c.index(8)) #qual é a posição do número 8 (no caso, na tupla c)
print(c.index(5, 1)) #se houver dois números iguais, o programa vai considerar a posição da primeira ocorrência. No entanto, caso você queira uma posição específica para um mesmo número/item (no caso o 5), você pode separar por vírgula o número que vc escolheu e a posição seguinte.

#Diferença entre JAVA e PYTHON.
#No JAVA, por exemplo, vc só pode declarar um tipo, exemplo: pessoa = ('Maria', 'João', 'Totó') ou pessoa = (1, 2, 3). Já no PYTHON você pode declarar strings e números na mesma variável. Veja só:

pessoa = ('Maria', 30, 'F', 70.6)
del(pessoa) #del apaga todos os dados da variável

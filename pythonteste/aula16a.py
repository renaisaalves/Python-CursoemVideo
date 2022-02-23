#AULA16 = TUPLAS ()
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche) #exibe todas as posições da tupla
print(lanche[0:3]) #começa na posição 0 [Hambúruger] e vai até a posição 2 [Pizza]
print(lanche[3]) #exibe a posição 3 [Pizza]
print(lanche[-2]) #conta da direita para a esquerda
print(len(lanche)) #mostra quantas posições existem na variável

for comida in lanche:
    print(f'Eu vou comer {comida}.')

#Também dá pra fazer dessa forma:
#for cont in range(0, len(lanch):
#    print(lanche[cont] ou f'{lanche[cont]} {cont}')
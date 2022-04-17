#AULA FEITA POR MIM

#Vamos adicionar listas dentro de uma lista! 

#LISTA CRIADA A PARTIR DOS DADOS INSERIDOS PELO USUÁRIO

lista1 = list()
lista1.append('Maria')
lista1.append(20)
print(lista1) #vai me retornar a lista inteira
print(lista1[0]) #vai me retornar o dado que ocupa a posição 0 na memória, nesse caso, 'Pedro'

lista2 = list()
lista2.append(lista1[:]) #eu sempre tenho que colocar [:] para as listas não ficarem idênticas!
print(lista2)

#Vou criar mais duas listas para adicionar na lista 2!

lista3 = ['João', 15]
lista4 = ['Ana', 50]
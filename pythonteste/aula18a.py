#AULA FEITA POR MIM

#Vamos adicionar listas dentro de uma lista! 

#LISTA CRIADA A PARTIR DOS DADOS INSERIDOS PELO USUÁRIO

lista1 = list()
lista2 = list()
lista3 = []

for c in range(0, 2):
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    if c == 1:
        lista1.append(name)
        lista1.append(age)
print(lista1)
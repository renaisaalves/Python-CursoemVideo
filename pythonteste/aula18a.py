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

lista2 = ['Carlos', 19], ['Ana', 32], ['João', 50]
print(lista2)
print(lista2[0][0])
print(lista2[1][2])
print(lista2[0][2])
print(lista2[1])

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
    
grupo = []
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #clear limpa os dados
print(galera)

totalmaior = totalmenor = 1
for p in grupo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1
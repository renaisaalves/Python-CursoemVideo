#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for c in range(0, 3):
    val = int(input(f'Digite o {c}º valor: '))
    lista(val)
print(f'{lista.sort()}')

#Vamos supor que eu armazene um valor [4] em uma variável comum. Sabendo que a instrução está dentro de um laço, se eu não armazenar esse valor em uma lista ou em outra variável, na próximo laço eu vou perder esse valor. 

#A questão é: será que é possível armazenar todos os valores dentro de uma lista, para depois aplicar as técnicas específicas de listas, ou fazer pelo modo tradicional, armazenando um determinado valor em uma variável e aplicando os testes lógicos? 

#O primeiro passo já foi feito: o laço foi criado, já com o valor determinado pelo exercício [5], e os números já foram cadastrados dentro de uma lista. No entanto, os números aparecem na ordem que o usuário digita, pois não há nenhum outro comando que faça com que os números sofram alterações...

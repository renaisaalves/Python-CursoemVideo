#AULA17: LISTAS



num = [2, 5, 9, 3]
num[2] = 3 #A posição 2 vai deixar de ser um [9] e vai passar a valer [3]
num.append(7) #Vai adicionar o valor [7] na última posição da lista
num.sort() #Coloca os valores em ordem
num.sort(reverse=True) #Coloca os valores em ordem inversa
num.insert(2, 0) #Na posição 2, eu quero inserir um valor [0]
num.pop() #Elimina o último valor da lista [no caso, o valor 2]
num.pop(2) #Elimina o valor que ocupa a posição [2]
num.remove(3) #Quando há dois valores iguais, remove vai deletar o primeiro que ocorrer [no caso, o primeiro 3]
print(num)
print(f'Essa lista tem {len(num)} elementos.') #exibe quantos elementos existem na lista.
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
    
valores = [] #ou valores = list()

valores.append(5)
valores.append(4)
valores.append(9)

for c in valores:
    print(f'{c}...', end='')

for v, c in enumerate(valores):
    print(f'Na posição {v}, encontreo o valor {c}!')
print('Cheguei ao final da lista.')

#LER VALORES PELO TECLADO: 

for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    
#PECULIARIDADE DO PYTHON:

a = [2, 3, 4, 7]
b = a 

print(a)
print(b)

#Se eu alterar um valor, ambas as listas mudarão, pois b = a:

b[2] = 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')
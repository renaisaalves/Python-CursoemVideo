#ex027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip().title()
print('Muito prazer em te conhecer!')
nome = n.split()
print('Seu primeiro nome é {}.' .format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))

#Importante: quando usamos split (lista) o programa conta por frase e não por palavra. Assim, 'Renaisa' 'Alves' 'Silva' possui 3 posições (0, 1, 2). Ao colocarmos 0, estaremos sempre indicando a primeira frase da lista.
#A dica de ouro começa agora: sempre que quiser usar a última frase/elemento da lista, coloque em número negativo. Assim, o programa começará a ler da direita para a esquerda. No caso, [Renaisa] = -3 [Alves] = -2 [Silva] = -1 
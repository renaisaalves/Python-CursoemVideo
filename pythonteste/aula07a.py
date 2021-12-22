#AULA 7: OPERADORES ARITMÉTICOS

nome = input('Qual é o seu nome?\n')
print('Prazer em te conhecer, {:20}.' .format(nome))
#Com :20, posso fazer 20 espaços (centralizado).
#Além disso, posso informar a direção desses espaços com :> (direita) ou :< (esquerda).

n1 = int(input('Um valor: '))
n2 = int(input('Outro número: '))
print('A soma vale {}' .format(n1 + n2))
#Soma rápida para mostrar na tela. 

n1 = int(input('Um novo valor: '))
n2 = int(input('Outro novo valor: '))
s = n1 + n2 
p = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2
print(' Soma: {}\n Produto: {}\n Divisão: {:.3f}\n' .format(s, p, d), end= ' ') 
print('Divisão inteira: {}\n Potência: {}\n' .format(di, e))
# end=' ' serve para não quebrar a linha. 
#Para quebrar linhas em uma string, use \n.
#:.2f = duas casas decimais flutuantes (pontos)




#ex050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

#Não consegui raciocinar pra fazer. 

#c vai se repetir 6 vezes (1, 7). 
#conforme vc digita um número, a variável 'num' recebe um novo valor. 
#Porém, ela vai atender a estrutura condicional 'if': se o resto da divisão do valor for igual a 0, ela vai contar e somar. 
#a variável 'soma' começa inicialmente com 0, mas vai armazenando valores através de uma adição entre ela mesma e a variável do número que atendeu à condição if. Por exemplo, vamos supor que você digita o número 4. 
# 4 é um número par, então vai atender a condição if. Nesse caso, o valor 4 (que foi armazenado na variável 'num') vai ser somado com a variável soma: soma (0) = soma (0) + num (4) => soma (4) = soma (4) + num (4)
#Isso acima aconteceu porque 4 + 0 = 4, e como a soma armazena uma adição, ela vai armazenar o número 4. 
#vamos supor que próximo número a ser digitado seja 18. Como 18 é um número par, ele vai atender a estrutura condicional if.
#soma (4) = soma (4) + num (18) => soma (22) = soma (22) + num (18)

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: ' .format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}.' .format(cont, soma))
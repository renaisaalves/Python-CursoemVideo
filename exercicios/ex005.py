#ex005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}' . format(n, (n-1), (n+1)))

#É possível criar 2 variáveis (uma para o antecessor e outra para o sucessor), no entanto, como é apenas um exercício simples, não houve a necessidade de criar variáveis. 
#Uma coisa importate é que, embora a operação seja realizada dentro dos parênteses afim de economizar memória, caso eu pricisasse do antecessor e sucessor, eu teria que criar obrigatoriamente uma variável afim de evitar dores de cabeça futuros. 
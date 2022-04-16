#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

frase = str(input('Digite uma frase que use parênteses.\nFrase: '))
if frase not in '()':
    print('Sua frase não possui parênteses.\nReescreva novamente: ')
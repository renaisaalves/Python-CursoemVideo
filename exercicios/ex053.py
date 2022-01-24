#ex053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#EXERCÍCIO DIFÍCIL 

frase = str(input('Digite uma frase: ')).strip().upper() #strip = tirei os espaços; upper = tudo em letra maiúscula
palavras = frase.split() #split = criei uma lista
junto = ''.join(palavras) #juntei as palavras (sem espaços)
inverso = ''
for letra in range(len(junto) -1, -1, -1): #busquei as palavras, mas não entendi a ordem de repetição
    inverso = inverso + junto[letra] #juntei duas variáveis / a que está sem nada + frase
    print(junto, inverso)
if inverso == junto:
    print('É um PALÍNDROMO!')
else:
    print('NÃO É um PALÍNDROMO!')
    
#OBS: Existe uma maneira muito mais fácil de fazer isso sem precisar do laço de repetição 'for'. Basta apagar o laço e escrever inverso = junto[::-1]
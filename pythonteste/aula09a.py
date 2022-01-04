#AULA9 - FUNCIONALIDADES DA STRING 

frase = 'Curso em Video Python'
print(len(frase)) #indica a quantidade de posições que a variável possui (no caso, Curso em Video Python possui 21)
print(frase[::2]) #pula 2 casas 
print(frase[9:20:2]) #exibe somente os caracteres das posições 9 até 20, pulando 2 casas
print(frase[:5]) #exibe os caracteres que começam da posição 0 até 4
print(frase[15:]) #exibe os racteres da posição 15 até o final 
print(frase[9::3]) #exibe somente os caracteres das posições 9 até o final, pulando 3 casas 
print(frase.find('Python')) #encontra a posição que começa os caracteres Python
print(frase.count('o')) #conta quantos caracteres 'o' existem dentro da variável
print(frase.upper()) #coloca tudo em maiúsculo
print(frase.lower()) #coloca tudo em minúsculo 
print(frase.capitalize()) #somente o primeiro caracter (posição 0) vai estar em maiúsculo
print(frase.title()) #todos os caracteres que iniciam após o espaço estarão em maiúsculo
print(frase.strip()) #elimina espaços inúteis (sem nada)
print(frase.split()) #quebra as frases em pedaços (a quebra é feita em cada espaço da variável)
print(''.join(frase)) #junta novamente os pedaços.
print(frase.replace('Python', 'Android')) #troca uma palavra pela outra, no caso 'Python' por 'Android'
print('Curso' in frase)

print(frase.lower().find('video'))
divido = frase.split() 
print(divido[2][3])

print("""Caso eu queira escrever uma frase muito longa e um texto, ao invés de aspas simples, eu posso usar aspas triplas.""")
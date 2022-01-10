#AULA 11 - CORES NO TERMINAL

#CÓDIGO PYTHON: \033[x;xx;xxm
#STYLE: 0 (none); 1 (bold); 4 (underline); 7 (negative/inversão)
#TEXT: 30 (white); 31 (red); 32 (green); 33 (yellow); 34 (blue); 35 (purple); 36 (cian); 37 (gray)
#BACKGROUND: 40 (white); 41 (red); 42 (green); 43 (yellow); 44 (blue); 45 (purple); 46 (cian); 47 (gray)

print('\033[0;30;41mOlá, Mundo!\033[m')
print('\033[4;33;46mEstou fazendo alguns testes no terminal.\033[m')
print('\033[1;45;33mMuitas cores podem ser usadas para estilizar o texto.\033[m')
print('\033[0;30;42mQuando não há configuração de estilo, não é preciso informar 0.\033[m')
print('\033[1;31;43mPara fundo preto e letra branca, não precisa informar nada,\npois já é a configuração padrão do terminal.\033[m')
print('\033[1;30;44mO estilo 7 é uma inversão de cor, então o preto passará a ser branco, dando efeito contrário.\033[m')

a = 3 
b = 5
print('Os valores são \033[1;31m{}\033[m e \033[1;33m{}\033[m!' .format(a, b))

#Caso você queira algo mais organizado, podemos fazer assim:

nome = str(input('Olá! Digite seu nome: '))
cores = {'limpa': '\033[m', 
         'blue': '\033[34m', 
         'yellow': '\033[33m', 
         'red': '\033[31m', 
         'green': '\033[32m'}

print('Prazer em te conhecer, {}{}{}!' .format('\033[1;34m', nome, '\033[m'))

#ou utilizando as variáveis da lista:

print('Muito prazer em te conhecer, {}{}{}!' .format(cores['red'], nome, cores['limpa']))
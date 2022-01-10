#AULA6 - ESTRUTURAS CONDICIONAIS ANINHADAS: IF, ELIF, ELSE

nome = str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Renaisa':
    print('Que nome bonito, {}{}{}! Tenha um bom dia!' .format('\033[1;33m', nome, '\033[m'))
elif nome == 'Maria' or nome == 'João' or nome == 'Ana' or nome == 'Antonio':
    print('Seu nome é bem popular no Brasil, {}{}{}. Tenha um bom dia!' .format('\033[1;31m', nome, '\033[m'))
elif nome in 'Cláudia, Paula, Juliana, Rayssa':
    print('Que nome feminino bonito, {}{}{}!' .format('\033[1;35m', nome, '\033[m'))
else: 
    print('Seu nome é muito comum...')
    print('Tenha um bom dia, {}{}{}!' .format('\033[1;32m', nome, '\033[m'))
print('Tchau!')

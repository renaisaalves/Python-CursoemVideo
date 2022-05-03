#DICIONÁRIOS

#Há duas maneiras de declarar um dicionário:
variavel = dict()
variavel = {}

#Dentro do dicionário, eu posso adicionar elementos. Esses elementos são conhecidos como chaves (keys) e valores (values):
variavel = {'nome':'Pedro', 'idade':25}
print(variavel['nome'])
#Vale lembrar que para declarar uma key (o nome de um índice), eu preciso colocar os dois pontos. 'Pedro' e 25 são os meus valores. Se eu der um print na tela, terei como retorno: Pedro.

#E se eu quiser adicionar mais um item no meu dicionário? Simples. Basta eu inserir:
variavel['sexo']='M'
#O que está dentro do colchetes é a minha key/índice, já o que está pra fora é o meu valor. 
# Eu também posso deletar um item do meu dicionário, por exemplo:
del variavel['idade']

#Vamos imaginar que eu tenha um dicionário de um filme:
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values()) #vai imprimir os valores ('Star Wars', 1977, 'George Lucas')
print(filme.keys()) #vai imprimir as chaves ('titulo', 'ano', 'diretor')
print(filme.items()) #vai imprimir o dicionário todo. 

#ESTRUTURA DE REPETIÇÃO

#Com o meu dicionário criado, eu posso usar o laço para representar os meus dados.
for k, v in filme.items():
    print(f'O {k} é {v}')
    
#k = representa os índices. Então sempre o primeiro do for estará relacionado ao índice. Dessa forma, o nome do primeiro índice é 'titulo', o nome do segundo índice é 'ano' e o nome do terceiro índice é 'diretor' e assim sucessivamente. Isso serve para qualquer estrutura. Guarde que o índice nos dicionários são conhecidos como keys. 
#v = representa os valores (values). O segundo do for (após a vírgula) estará relacionado aos valores. Nesse exemplo, o primeiro valor é 'Star Wars', o segundo valor é 1977 e o terceiro valor é 'George Lucas'.

#COLOCANDO DICIONÁRIOS DENTRO DE LISTAS

#É possível colocar dicionários dentro de listas! Vamos ver como isso funciona na prática.
locadora = []
locadora.append(filme)
print(locadora)

#Se eu quiser exibir um determinado item da minha lista, farei dessa forma:
print(locadora[0]['ano']) #1977
print(locadora[2]['titulo']) #Matriz
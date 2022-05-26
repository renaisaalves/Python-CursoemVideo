#ex095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = dict()
gols = list()

dados['jogador:'] = str(input('Nome: ')).capitalize()
partidas = int(input('Nº de partidas: '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols você fez na {c} partida? ')))


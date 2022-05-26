#ex095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = dict()
gols = list()
total = list()

while True:
    dados['jogador'] = str(input('Nome: ')).capitalize()
    dados['partidas'] = int(input('Nº de partidas: '))
    for c in range(dados['partidas']):
        dados['gols'] = int(input('Gol na {c}ª partida: '))
    dados['total'] = sum(total)
    resp = str(input('Quer adicionar mais um jogador? [S/N]: '))[0].upper()
    if resp not in 'S':
        break

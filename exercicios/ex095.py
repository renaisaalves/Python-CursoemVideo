#ex095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = dict()
while True:
    dados['jogador'] = str(input('Nome: ')).capitalize()
    resp = str(input('Quer adicionar mais um jogador? [S/N]: '))[0].upper()
    if resp not in 'S':
        break

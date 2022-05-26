#ex095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = dict()
gols = list()
cadastro = list()

while True:
    dados['jogador'] = str(input('Nome: ')).capitalize()
    partidas = int(input('Nº de partidas: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols você fez na {c+1}ª partida? ')))
    dados['gols'] = gols
    dados['total de gols'] = sum(gols)
    cadastro.append(dados.copy())
    dados.clear()
    resp = str(input('Quer adicionar mais um jogador? [S/N]: ')).upper()[0]
    if resp not in 'S':
        break
print(cadastro)


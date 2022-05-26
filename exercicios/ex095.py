#ex095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = dict()
gols = list()
cadastro = list()

while True:
    dados['jogador'] = str(input('Nome: ')).capitalize()
    partidas = int(input('Nº de partidas: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols você fez na {c} partida? ')))
    dados['gols'] = gols
    dados['total'] = sum(gols)
    print(dados)
    for c, v in dados.items():
        print(f'O campo {c} tem o valor {v}')
    cadastro.append(dados.copy())
    dados.clear()
    resp = str(input('Quer adicionar mais um jogador? [S/N]: ')).upper()[0]
    if resp not in 'S':
        break
print(cadastro)
'''print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for c, g in enumerate(gols):
    print(f'Na partida {c+1}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols.')
print('=' * 30)'''
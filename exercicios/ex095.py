#ex095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#INACABADO 

dados = dict()
gols = list()
time = list()

while True:
    dados.clear()
    nome = str(input('Nome: ')).capitalize()
    partidas = int(input('Nº de partidas: '))
    for c in range(partidas):
        gol = int(input(f'Quantos gols você fez na {c} partida? '))
        gols.append(gol)
    total = sum(gols)
    dados = {'jogador': nome, 'gols': gols, 'total': total}
    time.append(dados.copy())
    print('=' * 30)
    print(dados)
    print('=' * 30)
    for c, v in dados.items():
        print(f'O campo {c} tem o valor {v}')
    print('=' * 30)
    print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
    for c, g in enumerate(gols):
        print(f'Na partida {c}, fez {g} gols.')
    print(f'Foi um total de {total} gols.')
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resp not in 'S':
        break
print('=' * 30)
print('FIM DO PROGRAMA')
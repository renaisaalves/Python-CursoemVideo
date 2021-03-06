#ex093:  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = list()

nome = str(input('Nome: ')).capitalize()
partidas = int(input('Nº de partidas: '))
for c in range(partidas):
    gol = int(input(f'Quantos gols você fez na {c} partida? '))
    gols.append(gol)
total = sum(gols)
dados = {'jogador': nome, 'gols': gols, 'total': total}
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
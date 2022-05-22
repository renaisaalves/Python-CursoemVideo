#ex093:  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = list()
total = 0

nome = str(input('Nome: ')).capitalize()
partidas = int(input('Nº de partidas: '))
for c in range(partidas):
    gol = int(input(f'Quantos gols você fez na {c} partida? '))
    gols.append(gol)
    total = total + gol
dados = {'jogador': nome, 'gols': gols, 'total': total}


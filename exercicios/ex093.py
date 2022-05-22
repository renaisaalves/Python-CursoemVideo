#ex093:  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
total = 0

jogador = str(input('Nome: ')).capitalize()
partidas = int(input('Nº de partidas: '))
for c in range(partidas):
    gols = int(input(f'Quantos gols você fez na {c} partida? '))
    total = total + gols
dados['jogador': jogador, 'partidas': partidas, 'total': total]
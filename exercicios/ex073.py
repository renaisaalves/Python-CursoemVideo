#ex073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

print('='  * 40)
print('CAMPEONATO BRASILEIRO DE FUTEBOL (2022)')
print('='  * 40)

rank = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 
        'Atlético MG', 'Atlético PR', 'Cruzeiro', 'Botafogo', 'Santos', 
        'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 
        'Vasco', 'Sport', 'América MG', 'Vitória', 'Paraná')

print(f'OS SEIS PRIMEIROS COLOCADOS:\n{rank[0:6]}')
print('-'  * 40)
print(f'OS QUATRO ÚLTIMOS COLOCADOS:\n{rank[16:21]}')
print('-'  * 40)
print('LISTAGEM EM ORDEM ALFABÉTICA:\n',sorted(rank))
print('-'  * 40)
print('POSIÇÃO DO TIME CHAPECOENSE:\n',rank.index('Chapecoense'))
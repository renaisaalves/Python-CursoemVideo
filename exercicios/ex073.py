#ex073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

print('='  * 40)
print('CAMPEONATO BRASILEIRO DE FUTEBOL (2022)')
print('='  * 40)

rank = ('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')

print(rank[0:6])
print(rank[16:21])
print(sorted(rank))
print(rank.index())
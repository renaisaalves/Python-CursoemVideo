#ex073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

#MEU EXERCÍCIO COM ATUALIZAÇÕES

print('='  * 40)
print('CAMPEONATO BRASILEIRO DE FUTEBOL (2022)')
print('='  * 40)

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 
        'Atlético MG', 'Atlético PR', 'Cruzeiro', 'Botafogo', 'Santos', 
        'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 
        'Vasco', 'Sport', 'América MG', 'Vitória', 'Paraná')

print(f'OS CINCO PRIMEIROS COLOCADOS:\n{times[0:5]}')
print('-'  * 40)
print(f'OS QUATRO ÚLTIMOS COLOCADOS:\n{times[16:21]}') #ou [-4]
print('-'  * 40)
print(f'LISTAGEM EM ORDEM ALFABÉTICA:\n{sorted(times)}')
print('-'  * 40)
print(f'POSIÇÃO DO TIME CHAPECOENSE:\n {times.index("Chapecoense")}')
#ex024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em qual cidade você nasceu?\n')).strip()
print(cidade[:5].capitalize() == 'Santo')

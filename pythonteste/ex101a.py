#ex101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(year):
    if year <= 15:
        print(f'Voto NEGADO.')
    elif year >= 16 and year <= 17:
        print(f'Voto OPCIONAL.')
    elif year >= 70:
        print(f'Voto OPCIONAL.')
    else:
        year >= 18 and year < 70
        print(f'Voto OBRIGATÓRIO.')
    pass
#ex101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade <= 15:
        print(f'Idade: {idade} | Voto NEGADO.')
    elif idade >= 16 and idade <= 17:
        print(f'Idade: {idade} | Voto OPCIONAL.')
    elif idade >= 70:
        print(f'Idade: {idade} | Voto OPCIONAL.')
    else:
        idade >= 18 and idade < 70
        print(f'Idade: {idade} | Voto OBRIGATÓRIO.')

nasc = int(input('Ano de nascimento: '))
voto(nasc)
#ex069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# quantas pessoas tem mais de 18 anos.
# quantos homens foram cadastrados.
# quantas mulheres tem menos de 20 anos.

#FEITO POR MIM

pessoa = homem = mulher = 0

while True:
    print('=' * 15)
    print('CADASTRO BÁSICO')
    print('=' * 15)
    idade = int(input('Informe uma idade: '))
    while idade < 0 or idade > 200: 
        idade = int(input('Inválido. Informe uma idade real: '))
    sexo = str(input('Informe o gênero [F/M]: ')).strip().upper()
    while sexo not in 'F/M':
        sexo = str(input('Inválido. Informe o gênero novamente [F/M]: ')).strip().upper()
    if idade >= 18: 
        pessoa = pessoa + 1 
    if sexo in 'M':
        homem = homem + 1 
    if sexo in 'F' and idade < 20:
        mulher = mulher + 1
    resposta = str(input('Deseja continuar? [Sim/Não]: '))
    if resposta not in 'NãonaonNAONÃOnãoSimsimsSIMss':
        resposta = str(input('Informação inválida. Digite [Sim/Não]: '))
    if resposta in 'NãonaonNAONÃOnão':
        break
print('=' * 30)
print(f'{pessoa} pessoas tem mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulher} mulheres tem menos de 20 anos.')
print('=' * 30)

#PROFESSOR GUANABARA
tot18 = totH = totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('')).strip().upper()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        totH = totH + 1
    if sexo == 'F' and idade < 20:
        totM20 = totM20 + 1 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
#ex069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# quantas pessoas tem mais de 18 anos.
# quantos homens foram cadastrados.
# quantas mulheres tem menos de 20 anos.

pessoa = 0
homem = 0
mulher = 0

while True:
    idade = int(input('Informe uma idade: '))
    while idade < 0 or idade > 200: 
        idade = int(input('Inválido. Informe uma idade real: '))
    sexo = str(input('Informe o gênero [F/M]: ')).strip().upper()
    while sexo not in 'F/M':
        sexo = str(input('Inválido. Informe o gênero novamente [F/M]: ')).strip().upper()
    if idade > 18: 
        pessoa = pessoa + 1 
    if sexo in 'M':
        homem = homem + 1 
    if sexo in 'F':
        if idade < 20:
            mulher = mulher + 1
    resposta = str(input('Deseja continuar? [Sim/Não]: '))
    if resposta not in 'NãonaonNAONÃOnãoSimsimsSIMss':
        resposta = str(input('Informação inválida. Digite [Sim/Não]: '))
    if resposta in 'NãonaonNAONÃOnão':
        break
print(f'{pessoa} pessoas tem mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulher} mulheres tem menos de 20 anos.')
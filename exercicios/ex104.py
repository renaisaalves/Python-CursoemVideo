#ex104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
    n = str(input('Digite um n: '))
    if n.isnumeric() == True:
        print(f'Você acabou de digitar o número {n}')
    elif n == None:
        print(f'Você não digitou nada.')
    else:
        print(f'Você digitou um valor NÃO numérico.')
leiaInt()
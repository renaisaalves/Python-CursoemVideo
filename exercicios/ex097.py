#ex097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  

def escreva():
    print('=' * 20)
    print(f'{"Hello, World!":^20}')
    print('=' * 20)
escreva()
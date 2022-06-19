#ex106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores

def interactive_help(com):
    help(com)
    
def colors(msg):
    red = print('\033[1;31m', msg, '\033[m')
    green = print('\033[1;32m', msg, '\033[m')
    yellow = print('\033[1;33m', msg, '\033[m')
    blue = print('\033[1;34m', msg, '\033[m')
    purple = print('\033[1;35m', msg, '\033[m')
    cian = print('\033[1;36m', msg, '\033[m')
    white = print('\033[1;37m', msg, '\033[m')

while True:
    comando = str(input('Digite um comando: '))
    if comando == 'fim':
        break
    interactive_help(comando)
colors()

    


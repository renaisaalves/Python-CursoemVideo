#ex106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores

def interactive_help(com):
    help(com)

comando = str(input('Digite um comando: '))
interactive_help()
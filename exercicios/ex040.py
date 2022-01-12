#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média foi {}. Portanto, você está {}REPROVADO{}.' .format(media, '\033[1;31m','\033[m'))
elif media > 5.0 and media <= 6.9:
    print('Sua média foi {}. Portanto, você está de {}RECUPERAÇÃO{}.' .format(media, '\033[1;33m','\033[m'))
else:
    media > 7.0 
    print('Sua média foi {}. Portanto, você está {}APROVADO{}.' .format(media, '\033[1;32m','\033[m'))
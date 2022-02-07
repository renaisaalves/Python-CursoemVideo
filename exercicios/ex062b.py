#62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

#FEITO POR MIM

print('Gerador de PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} ➝ ' .format(termo), end=' ')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a amais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))
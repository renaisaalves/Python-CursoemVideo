#62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

#FEITO POR MIM

print('Gerador de PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} ➝ ' .format(termo), end=' ')
    termo = termo + razao
    contador = contador + 1
print('FIM')


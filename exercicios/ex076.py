#ex076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#NÃO SOUBE FAZER

print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
lista = ('Smartphone', 2000, 'Notebook', 3500, 'Fone de Ouvido', 300, 'Bombom', 2.50)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else: 
        print(f'R${lista[pos]:>8.2f}')
        
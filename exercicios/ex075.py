#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

for c in range(1, 5):
    num = int(input(f'Digite o {c}º valor: '))
print(num)
print(num.count(9))
print(num.index(3))
print()
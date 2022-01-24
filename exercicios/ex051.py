#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)

#MEU RACIOCÍNIO / não consegui colocar o 1º termo

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(1, 11):
    a1 = a1 + r
    print('➝ ', a1, end=' ')
print('ACABOU')
    
#RACIOCÍNIO DO GUANABARA

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao #fórmula para calcular o enésimo termo

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' ➝  ')
print('ACABOU')
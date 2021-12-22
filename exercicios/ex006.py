#ex006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.' .format(n, d))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.' .format(n, t, n, r))

#:.2f = duas casas decimais flutuantes (pontos)

n = int(input('Digite outro número: '))
print('O dobro de {} vale {}.' .format(n, n*2))
print('O triplo de {} vale {}.\n A raiz quadrada de {} é igual a {:.2f}.' .format(n, n*3, n, n**(1/2)))

#A potência pode ser usada de outra forma, através de pow(n, (1/2))
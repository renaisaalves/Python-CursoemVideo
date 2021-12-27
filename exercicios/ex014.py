#ex014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em ºC:\n'))
f = ((9 * c) / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF' .format(c, f))

#Os parênteses servem para delimitar a ordem da conta, ou seja, o que vai ser realizado primeiro. 
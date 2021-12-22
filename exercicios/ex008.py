#ex008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Escreva uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {} corresponde a {} centímetros e {} milímetros.' . format(medida, cm, mm))
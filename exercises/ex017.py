from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = hypot(co, ca)
print(f'A hipotenusa do triângulo de catetos {co} e {ca} é igual a {h}')

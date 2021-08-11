def area(l, c):
    a = l * c
    return a


largura = float(input('Largura do terreno (m): '))
comprimento = float(input('Comprimento do terreno (m): '))
a = area(largura, comprimento)
print(f' O terreno de {largura:.1f}x{comprimento:.1f} tem área de {a:.1f}m')

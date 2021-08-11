def ex053():
    frase = input('Digite uma frase:\n').strip().upper().split()
    palavras = ''.join(frase)
    inverso = ''
    for i in range(len(palavras)-1, -1, -1):
        inverso += palavras[i]
    if inverso == palavras:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')
    

ex053()

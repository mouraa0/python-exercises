def ex026():
    frase = input('digite uma frase: ').strip().upper()
    letra = 'A'

    print(f'A letra "{letra}" aparece {frase.count(letra)} vez(es) na frase.')
    print(f'A primeira letra "{letra}" apareceu na posição {frase.find(letra)+1}')
    print(f'A última letra "{letra}" apareceu na posição {frase.rfind(letra)+1}')


ex026()

from random import randint

def sorteia():
    lista = []
    
    for i in range(5):
        lista.append(randint(1, 10))
    
    print(lista)
    
    return lista

def somaPar(l):
    somador = 0
    
    for i in l:
        if i % 2 == 0:
            somador += i
    
    print(f'Soma dos números pares sorteados: {somador}')


lista = sorteia()
somaPar(lista)

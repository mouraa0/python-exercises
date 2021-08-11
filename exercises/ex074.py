from random import randint

def ex074():
    numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    maior = 0
    menor = None
    for i in numeros:
        print(i)
        if menor is None:
            menor = i
        elif i < menor:
            menor = i
        if i > maior:
            maior = i
    print(f'Maior número gerado: {maior}\nMenor número gerado: {menor}')


ex074()

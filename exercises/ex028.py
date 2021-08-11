from random import randint
def ex028():
    n = randint(0,6)
    res = int(input('Número entre 0 e 5: '))
    if res == n:
        print('Você acertou!')
    else:
        print(f'Você errou! Número correto: {n}')


ex028()

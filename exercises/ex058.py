from random import randint
def ex058():
    num = randint(0,10)
    tentativa = int(input('Digite um número: '))
    while num != tentativa:
        tentativa = int(input('Você errou! Tente novamente: '))
    print('Você acertou!')


ex058()

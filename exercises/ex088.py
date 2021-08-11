from random import randint

def ex088():
    qtd = int(input('Quantos jogos você deseja gerar?\n'))
    temp = []
    geral = []

    for i in range(qtd):
        for j in range(6):
            temp.append(randint(1,60))
            temp.sort()
        geral.append(temp[:])
        temp.clear()

    for i in range(qtd):
        print(f'{i + 1}º Jogo: {geral[i]}')


ex088()

def ex055():
    pesomax = 0
    pesomin = 0
    
    for i in range(1,6):
        peso = float(input(f'Digite o peso da {i}ª pessoa: '))
        if i == 1:
            pesomax = peso
            pesomin = peso
        if peso > pesomax:
            pesomax = peso
        elif pesomin > peso:
            pesomin = peso
    print(f'Maior peso: {pesomax}KG\nMenor peso: {pesomin}KG')


ex055()

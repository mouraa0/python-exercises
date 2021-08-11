def ex067():
    while True:
        numero = int(input('Número:\n'))
        if numero < 0:
            break
        for i in range(1, 11):
            print(f'{numero} x {i} = {numero * i}')


ex067()

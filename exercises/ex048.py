def ex048():
    somatorio, contador = 0, 0
    for i in range(1,501,2):
        if i % 3 == 0:
            contador += 1
            somatorio = somatorio + i
    print(f'Contador: {contador}\nSomatório: {somatorio}')


ex048()

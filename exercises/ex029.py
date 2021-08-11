def ex029():
    vel = float(input('Velocidade: '))
    velmax = 80
    custo = 7
    
    if vel > velmax:
        multa = (vel-velmax)*custo
        print(f'Velocidade não permitida! Multa: R${multa:.2f}')
    else:
        print('Velocidade permitida!')


ex029()

def contador(a, b, c):
    if a > b:
        c = -c
        for i in range(a, b - 1, c):
            print(f'{i}', end=' ')
        print('')
    
    elif a < b:
        for i in range(a, b + 1, c):
            print(f'{i}', end=' ')
        print('')
    print('='*30)


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

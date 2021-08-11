def maior(*num):   
    maior = 0
    for i in num:
        if i > maior:
            maior = i
        print(f'{i}', end=' ')
    print('')
    
    print(f'Ao todo foram {len(num)} números\nMaior número: {maior}')
    print('='*30)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
        
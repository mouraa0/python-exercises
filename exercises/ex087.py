def ex087():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    soma_par = 0
    soma_ter = 0    
    maior_seg = 0
    
    for i in range(3):
        for j in range(3):
            matriz[i][j] = int(input(f'Digite um valor para [{i + 1}, {j + 1}]: '))
            
            if matriz[i][j] % 2 ==0:
                soma_par += matriz[i][j]
            
            if i == 1:
                if maior_seg < matriz[i][j]:
                    maior_seg = matriz[i][j]
            
            if j == 2:
                soma_ter += matriz[i][j]
            
    for i in range(3):
        for j in range(3):
            print(f'[{matriz[i][j]:^5}]',end='')
        print()
    print('='*30)
    print(f'Soma de todos os pares digitados: {soma_par}\nSoma dos valores da terceira coluna: {soma_ter}\nMaior valor da segunda linha: {maior_seg}')


ex087()

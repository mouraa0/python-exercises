def ex085():
    pares = []
    impares = []
    geral = []
    
    for i in range(7):
        num = int(input(f'Digite o {i + 1}º número: '))
        
        if num % 2 == 0:
            pares.append(num)
            
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    geral.append(pares)
    geral.append(impares)        
    
    print(f'Pares digitados: {geral[0]}\nÍmpares digitados: {geral[1]}')


ex085()

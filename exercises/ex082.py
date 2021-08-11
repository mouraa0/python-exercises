def ex082():
    numeros = []
    pares = []
    impares = []
    condicao = 'S'
    
    while condicao == 'S':
        num = int(input('Digite um número: '))
        numeros.append(num)
        
        if num % 2 == 0:
            pares.append(num)
        
        else:
            impares.append(num)
        
        condicao = input('Deseja continuar? [S/N]\n').upper()
    
    print(f'Números digitados: {numeros}\nNúmeros pares: {pares}\nNúmeros ímpares: {impares}')


ex082()

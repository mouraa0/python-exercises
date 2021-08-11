def ex081():
    numeros = []
    condicao = 'S'
    qtd = 0
    
    while condicao == 'S':
        numeros.append(int(input('Digite um número: ')))
        condicao = input('Deseja continuar? [S/N]\n').upper()
    
    numeros.sort(reverse=True)
    
    if 5 in numeros:
        resultado = 'SIM'
    else:
        resultado = 'NÃO'

    print(f'Quantidade de números digitados: {len(numeros)}')
    print(f'Números digitados em ordem decrescente: {numeros}')
    print(f'O número 5 foi digitado? {resultado}')
    
    
ex081()

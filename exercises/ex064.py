def ex064():
    numereco = 0
    soma = 0
    contador = 0
    
    while numereco != 999:
        numereco = int(input('Digite um número (para encerrar digite 999):\n'))
        
        if numereco != 999:
            soma += numereco
            contador += 1
    
    print(f'{contador} números foram digitados\nSoma: {soma}')


ex064()
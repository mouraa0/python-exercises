def ex066():
    soma = 0
    contador = 0
    
    while True:
        numero = int(input('Digite um número (999 para parar): '))
        
        if numero == 999:
            break
        
        soma += numero
        contador += 1
    
    print(f'{contador} números foram digitados, a soma total é igual a {soma}.')


ex066()

def ex060():
    numero = int(input('Digite o número:\n'))
    contador = 1
    
    for i in range(1, (numero + 1)):
        contador *= i
    print(f'{numero}! = {contador}')


ex060()

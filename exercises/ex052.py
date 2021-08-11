def ex052():
    numero = int(input('Número:\n'))
    contador = 0
    
    for i in range(2, numero):
        if numero % i == 0:
            contador += 1
    if contador != 0:
        print('Não é primo')
    else:
        print('É primo')    

ex052()

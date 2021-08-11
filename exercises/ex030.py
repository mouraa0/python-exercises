def ex030():
    num = None
    while num != 0:
        num = int(input('Número:\n'))

        if num%2 != 0:
            print('Ímpar')
        else:
            print('Par')


ex030()

def ex05722():
    sexo = input('Digite seu sexo [M/F]: ')
    while sexo not in 'MF':
        sexo = input('Digite seu sexo corretamente [M/F]: ')

ex05722()

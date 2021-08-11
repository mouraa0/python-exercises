def leiaInt(msg):
    valor = 0
    condicao = 0
    while condicao is not True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            condicao = True
        else:
            print('ERRO! Digite um número inteiro válido.')
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')

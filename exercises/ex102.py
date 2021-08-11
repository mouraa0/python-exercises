def fatorial(a, show=False):
    c = 1
    for i in range(a, 0, -1):
        c *= i
        if show:
            print(f'{i}', end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ',end='')
      
    return c


num = int(input('Digite um número: '))
opcao = input('Deseja mostrar o processo? (vazio para não, True para sim): ')
print(fatorial(num,opcao))

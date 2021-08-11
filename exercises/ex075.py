def ex075():
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    valor3 = int(input('Digite outro valor: '))
    valor4 = int(input('Digite o último valor: '))
    numeros = (valor1, valor2, valor3, valor4)
    print(f'O valor 9 apareceu {numeros.count(9)} vez(es)\nO valor 3 apareceu na {(numeros.index(3)) + 1}ª Posição')
    for i in numeros:
        if i % 2 == 0:
            print(f'{i} é par')


ex075()

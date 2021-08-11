def ex079():
    qtd = int(input('Quantos números deseja digitar?\n'))
    numeros = []
    for i in range(qtd):
        num = int(input(f'Digite o {i + 1}º número: '))
        if num not in numeros:
            numeros.append(num)
    for c in sorted(numeros):
        print(f'{c}', end=' ')


ex079()

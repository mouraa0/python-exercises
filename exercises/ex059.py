def ex059():
    valor1 = float(input('Primeiro valor: '))
    valor2 = float(input('Segundo valor: '))
    op = 0
    while op != 5:
        op = input('Escolha:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valores\n[5] Fechar\n')
        while op not in ['1', '2', '3', '4', '5']:
            op = input('Escolha corretamente :\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valores\n[5] Fechar\n')
        op = int(op)
        if op == 1:
            resultado = (f'Soma: {valor1} + {valor2} = {valor1+valor2}')
        elif op == 2:
            resultado = (f'Multiplicação: {valor1} x {valor2} = {valor1*valor2}')
        elif op == 3:
            operacao = ['Maior', '>']
            if (valor1-valor2) > 0:
                resultado = (f'Maior: {valor1} > {valor2}')
            else:
                resultado = (f'Maior: {valor2} > {valor1}')
        elif op == 4:
            valor1 = float(input('Primeiro valor: '))
            valor2 = float(input('Segundo valor: '))

        if op != 5:
            print(resultado)


ex059()

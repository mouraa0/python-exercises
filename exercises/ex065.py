def ex065():
    contador = 0
    maior = 0 
    menor = None
    somatorio = 0
    condicao = 'S'
    while condicao == 'S':
        numero = int(input('Digite um número: '))
        contador += 1
        somatorio += numero
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero
        condicao = input('Deseja continuar? [S/N]: ').strip().upper()
    if somatorio > 0:
        print(f'Média dos números digitados: {somatorio/contador}\nMaior número digitado: {maior}\nMenor número digitado: {menor}')


ex065()

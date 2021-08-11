def ex050():
    somatorio = 0
    
    for i in range(1,7):
        num = int(input('Digite um número: '))
        if num % 2 == 0:
            print(f'{num} é par')
            somatorio += num
    print(f'A soma de todos os pares citado é igual a {somatorio}')


ex050()

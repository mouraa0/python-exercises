def ex069():
    condicao = None
    contador_18 = 0
    contador_20 = 0
    contador_homem = 0

    while condicao != 'S':
        idade = int(input('Idade da Pessoa:\n'))
        sexo = input('Sexo da pessoa[M/F]:\n').upper()
        
        if idade > 18:
            contador_18 += 1
        
        if sexo == 'M':
            contador_homem += 1
        
        elif sexo == 'F':
            
            if idade < 20:
                contador_20 += 1
        
        condicao = input('Deseja parar? [S/N]: ').upper()
    
    print(f'Pessoas com mais de 18 anos: {contador_18}'
    f'\nHomens cadastrados: {contador_homem}\nMulheres com menos 20 anos: {contador_20}')


ex069()

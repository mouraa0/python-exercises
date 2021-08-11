def ex041():
    nascimento = int(input('Ano de nascimento:\n'))
    ano_atual = 2021
    idade = ano_atual - nascimento
    print(f'O atleta tem {idade} anos')
    
    if idade <= 9:
        classi = 'MIRIM'
    elif idade > 25:
        classi = 'MASTER'
    elif idade <= 14:
        classi = 'INFANTIL'
    elif idade <= 19:
        classi = 'JÚNIOR'
    else:
        classi ='SÊNIOR'
    
    print(f'Classifição: {classi}')


ex041()


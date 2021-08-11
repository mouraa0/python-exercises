def ex054():
    ano_atual = 2021
    contma = 0
    contme = 0
    
    for i in range(1,8):
        data = int(input(f'Data de nascimento da {i}ª pessoa: '))
        if (ano_atual - data) < 18:
            contme += 1
        else:
            contma += 1
    print(f'{contma} pessoas são maiores de idade e {contme} são menores.')    


ex054()

def ex039():
    nas = int(input('Digite sua data de nascimento: '))
    ano_atual = 2021
    idade = ano_atual - nas
    print(f'Idade: {idade}')
    if idade == 18:
        print('Idade certa para se alistar.')
    elif idade > 18:
        print(f'Você deveria ter se alistado em {2021 - (idade - 18)}')
    else:
        print(f'Você deverá se alistar em {2021 + (18 - idade)}')


ex039()

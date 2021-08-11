def ex056():
    contador_idade = 0
    maior_idade = 0
    contador_mulheres = 0
    
    for i in range(1,5):
        nome = input(f'Nome da {i}ª pessoa: ')
        idade = int(input(f'Idade da {i}ª pessoa: '))
        sexo = input(f'Sexo da {i}ª pessoa[M/F]: ').upper()
        print('-'*10)
        contador_idade += idade
        if sexo == 'M':
            if idade > maior_idade:
                maior_idade = idade
                mais_velho = nome
        else:
            mais_velho = 'Não tem homens'
            if idade < 20:
                contador_mulheres += 1
    media_idade = contador_idade/4
    print(f'Média de idade: {media_idade:.0f}\nHomem mais velho: {mais_velho}\nMulheres com menos de 20 anos: {contador_mulheres}')


ex056()

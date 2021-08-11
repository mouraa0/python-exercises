def ex040():
    n1 = float(input('Primeira nota:\n'))
    n2 = float(input('Segunda nota:\n'))
    media = (n1+n2)/2
    print(media)
    
    if media >= 7:
        print('Aprovado')
    elif media < 5:
        print('Reprovado')
    else:
        print('Recuperação')


ex040()

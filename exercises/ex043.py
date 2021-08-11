def ex043():
    peso = float(input('Seu peso:\n'))
    altura = float(input('Sua altura:\n'))
    imc = (peso)/(altura*altura)
    
    print(f'IMC: {imc:.2f}')
    
    if imc < 18.5:
        situ = 'ABAIXO DO PESO'
    elif imc > 40:
        situ = 'ACIMA DO PESO'
    elif imc < 25:
        situ = 'PESO IDEAL'
    elif imc < 30:
        situ = 'SOBREPESO'
    else:
        situ = 'OBESIDADE'
    
    print(f'Situação: {situ}')


ex043()

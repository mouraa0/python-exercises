from random import randint

def tem_duplicatas():
    dicio = dict()
    numeros = list()

    
    for i in range(5):
        numeros.append(randint(0,1000))

    for i in numeros:
        if str(i) in dicio:
            return 'Tem!'
        
        else:
            dicio[f'{i}'] = i

    return 'Não tem!'


resultado = tem_duplicatas()
print(resultado)

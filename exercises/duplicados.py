from random import randint

def criar_array():
    n = []
    
    for i in range(1000):
        n.append(randint(1,100))
    
    return n

def tem_duplicatas(arr):
    dicio = dict()
    for i in arr:
        if str(i) in dicio:
            return True
        
        else:
            dicio[f'{i}'] = i

    return False


resultado = tem_duplicatas(criar_array())

if resultado:
    print('Tem!')

else:
    print('Não tem!')

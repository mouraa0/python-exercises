def wtf(l1):
    for i in range(len(l1) - 1):
        for j in range(len(l1) - 1):
            if l1[j] > l1[j + 1]: 
                l1[j], l1[j + 1] = l1[j + 1], l1[j]


def ex080():
    numeros = []
    
    for i in range(5):
        num = int(input(f'Digite o {i + 1}º número: '))
        numeros.append(num)
    
    wtf(numeros)
    print(numeros)


ex080()

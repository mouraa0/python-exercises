def ex078():
    lista = []
    maior = 0
    menor = None
    
    for i in range(5):
        lista.append(int(input('Digite um número: ')))
    
    for i in range(len(lista)):
        if menor == None:
            menor = lista[i]
            posmenor = i
        
        if lista[i] < menor:
            menor = lista[i]
            posmenor = i
        
        if lista[i] > maior:
            maior = lista[i]
            posmaior = i
    print(f'O maior número é {maior} e está na posição {posmaior}\nO menor número é {menor} e está na posição {posmenor}')


ex078()

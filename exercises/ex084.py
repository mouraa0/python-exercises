def ex084():
    temp = []
    lista_dados = []
    menor_peso = None
    maior_peso = 0
    nome_menorp = []
    nome_maiorp = []
    condicao = 'S'
    qtd = 0
    
    
    while condicao == 'S':
        qtd += 1
        temp.append(input(f'Digite o nome da {qtd}ª pessoa: '))
        temp.append(float(input(f'Digite o peso da {qtd}ª pessoa: ')))
        lista_dados.append(temp[:])
        temp.clear()
        condicao = input('Deseja continuar? [S/N]\n').upper()
        
        print('='*30)

    for i in lista_dados:
        if menor_peso is None:
            menor_peso = i[1]
        
        if menor_peso > i[1]:
            menor_peso = i[1]
            nome_menorp.clear()
            nome_menorp.append(i[0])
        
        elif menor_peso == i[1]:
            nome_menorp.append(i[0]) 
        
        elif maior_peso < i[1]:
            maior_peso = i[1]
            nome_maiorp.clear()
            nome_maiorp.append(i[0])
        
        elif maior_peso == i[1]:
            nome_maiorp.append(i[0])

    print(f'{len(lista_dados)} pessoas foram cadastradas.\n{menor_peso} foi o menor peso {nome_menorp}\n{maior_peso} foi o maior peso {nome_maiorp}')


ex084()

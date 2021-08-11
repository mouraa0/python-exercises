def ex094():
    geral = list()
    condicao = 'S'
    contador_idade = 0
    qtd_idade = 0
    lista_mulheres = list()
    lista_mediaup = list()
    
    while condicao == 'S':
        pessoa_fisica = dict()
        pessoa_fisica['Nome'] = input('Nome: ')
        pessoa_fisica['Sexo'] = input('Sexo: ').upper()
        pessoa_fisica['Idade'] = int(input('Idade: '))
        geral.append(pessoa_fisica)
        condicao = input('Deseja continuar? [S/N]\n').upper()
    
    for i in range(len(geral)):
        contador_idade += geral[i]['Idade']
        
        if geral[i]['Sexo'] == 'F':
            lista_mulheres.append(geral[i]['Nome'])
    
    media = contador_idade/len(geral)
    
    for i in range(len(geral)):
        if geral[i]['Idade'] > media:
            lista_mediaup.append(geral[i]['Nome'])
    
    print('='*30)
    print(f'{len(geral)} pessoas foram cadastradas\nMédia de idade: {media:.0f}\nMulheres: {lista_mulheres}\nPessoas com idade acima da média: {lista_mediaup}')


ex094()

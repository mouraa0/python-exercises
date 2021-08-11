def ex070():
    preco_total = 0
    maior = 0
    mais_barato = None
    condicao = 'S'
    
    while condicao == 'S':
        nome = input('Nome do produto: ')
        preco = float(input('Valor do produto: R$'))
        preco_total += preco
        
        if mais_barato is None:
            mais_barato = nome
            preco_barato = preco
        
        elif preco < preco_barato:
            preco_barato = preco
            mais_barato = nome
        
        if preco > 1000:
            maior += 1
        
        condicao = input('Deseja continuar? [S/N]: ').upper()
        
        print('-'*20)
    
    print(f'Preço total: R${preco_total:.2f}\nProdutos com mais de R$1000.00: {maior}\nProduto mais barato: {mais_barato}')
    


ex070()

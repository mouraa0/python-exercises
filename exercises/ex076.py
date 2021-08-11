def ex076():
    produtos = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 
    'Compasso', 'Mochila', 'Canetas', 'Livro', 1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
    for i in range(len(produtos) - 9):
        print(f'{produtos[i]:.<30}R${produtos[i + 9]:.2f}')


ex076()

def ex027():
    nome = input('Digite seu nome completo: ').strip().split()
    
    print(f'Seu primeiro nome é {nome[0]} e o seu último é {nome[len(nome)-1]}')


ex027()

def ex073():
    times = ('Palmeiras', 'Atlético Mineiro', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Ceará', 
    'Santos', 'Atlético Goianiense', 'Bahia', 'Corinthians', 'Fluminense', 'Juventude', 'Internacional', 
    'Sport', 'Cuiabá', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')
    
    for i in range(5):
        print(f'{i + 1}° Colocado: {times[i]}')
    
    print('=' * 20)
    
    for c in range(16, 20):
        print(f'{c + 1}° Colocado: {times[c]}')
    
    print('=' * 20)
    
    ordenado = sorted(times)
    
    for d in range(len(times)):
        print(ordenado[d])

    print('=' * 20)
    
    print(f'A Chapecoense está em {(times.index("Chapecoense")) + 1}° Lugar')


ex073()

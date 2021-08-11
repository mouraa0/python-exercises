def ex031():
    distancia = float(input('Digite a distância:\n'))
    diferencial = 200

    if distancia <= diferencial:
        custo = 0.5
    else:
        custo = 0.45
        
    print(f'Valor da viagem: R${(distancia*custo):.2f}')


ex031()

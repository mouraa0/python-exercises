def ex093():
    jogador = dict()
    gols = list()
    jogador['Nome'] = input('Nome do jogador: ')
    qtd = int(input(f'Quantos jogos {jogador["Nome"]} jogou: '))
    contador_gols = 0
    
    for i in range(qtd):
        gol_por_partida = int(input(f'Quantos gols foram marcados na {i + 1}ª partida: '))
        contador_gols += gol_por_partida
        gols.append(gol_por_partida)
    
    jogador['Gols'] = gols
    jogador['Total'] = contador_gols
    
    print('='*30)
    print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} jogos.')
    for i in range(len(jogador["Gols"])):
        print(f'Na {i + 1}ª partida, fez {jogador["Gols"][i]}')
    print(f'Marcou no total {jogador["Total"]} gols')


ex093()

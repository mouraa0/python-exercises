def inserir_jogador():
    jogador = dict()
    gols = list()
    contador_gols = 0
    
    jogador['Nome'] = input('Nome do jogador: ')
    qtd = int(input(f'Quantos jogos {jogador["Nome"]} jogou?: '))
    
    for i in range(qtd):
        gol = int(input(f'Gols na {i + 1}ª partida: '))
        contador_gols += gol
        gols.append(gol)
    
    jogador['Gols'] = gols
    jogador['Total'] = contador_gols

    return jogador

def mostrar_cadastro(cadastro):
    for i in range(len(cadastro)):
        print(f'{cadastro[i]["Nome"]}: {cadastro[i]["Total"]} gols no total\nCódigo = {i}')
        print('='*30)


def cadastrar_jogadores():
    cadastro_geral = list()
    condicao = 'S'
    
    while condicao == 'S':
        cad = inserir_jogador()
        cadastro_geral.append(cad)
        condicao = input('Deseja continuar? [S/N]\n').upper()
    
    return cadastro_geral

def mostrar_dados(cadastro):
    codigo = None
    
    while codigo != '':
        codigo = input('Código do jogador (Enter vazio para fechar): ')
        
        if codigo != '':
            codigo = int(codigo)
            
            if codigo <= (len(cadastro)-1):
                print(f'Dados de {cadastro[codigo]["Nome"]}')
                
                for i in range(len(cadastro[codigo]["Gols"])):
                    print(f'Gols na {i + 1}ª partida: {cadastro[codigo]["Gols"][i]}')
                    print('-'*30)
            else:
                print('Código errado!')
            
            print('='*30)

            
cadastro = cadastrar_jogadores()
mostrar_cadastro(cadastro)
mostrar_dados(cadastro)

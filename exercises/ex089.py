def recebe_nota():
    temp = []
    temp.append(input('Digite o nome do aluno: '))
    temp.append(float(input('Digite a primeira nota: ')))
    temp.append(float(input('Digite a segunda nota: ')))
    return temp


def mostra_boletim(notas):
    for i in range(len(notas)):
        media = ((notas[i][1])+(notas[i][2]))/2
        print(f'{notas[i][0]:.<20}{media:.2f}')


def gera_boletim():
    notas = []
    condicao = 'S'
    
    while condicao == 'S':
        notas.append(recebe_nota())
        condicao = (input('Deseja continuar? [S/N]\n')).upper()
        print('='*30)

    return notas


def mostra_nota(n1):
    condicao = input('Nome do Aluno (Para encerrar o programa, apenas dê enter vazio):\n')
    seg_condicao = None
    
    while condicao != '':
        for i in range(len(n1)):
            if n1[i][0] == condicao:
                print(f'Notas: {n1[i][1]:.2f}  ;  {n1[i][2]:.2f}')
        condicao = input('Nome do aluno (Para encerrar o programa, apenas dê enter vazio):\n ')


boletim = gera_boletim()
mostra_boletim(boletim)
mostra_nota(boletim)

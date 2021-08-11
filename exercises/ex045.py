from random import randint
def ex045():
    escolha = int(input('Suas opções:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA\n'))
    esc_maquina = randint(1,3)
    op_maq = ['PEDRA', 'PAPEL', 'TESOURA']
    print(esc_maquina)
    if (escolha - esc_maquina == 1) or (escolha - esc_maquina == (-2)):
        decisao = 'GANHOU'
    elif escolha == esc_maquina:
        decisao = 'EMPATOU'
    else:
        decisao = 'PERDEU'
    
    print(f'Escolha do computador: {op_maq[esc_maquina - 1]}\nVocê {decisao}')

ex045()


    

   

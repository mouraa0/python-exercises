from random import randint
def ex068oerrado():
    contador = 0
    op_maq = ['TESOURA', 'PAPEL', 'PEDRA']
    while True:
        esc_maq = randint(1,3)
        escolha = int(input('Suas opções:\n[1] TESOURA\n[2] PAPEL\n[3] PEDRA\n'))
        print(esc_maq)
        if (escolha - esc_maq == 1) or (escolha - esc_maq == (-2)):
            print(f'Você PERDEU!\nNúmero de vitórias: {contador}')
            break
        elif escolha == esc_maq:
            decisao = ('EMPATOU')
        else:
            decisao = ('GANHOU')
            contador += 1
        print(f'Você {decisao}')


ex068oerrado()

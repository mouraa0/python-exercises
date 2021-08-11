from random import randint
def ex068aa():
    contador = 0
    
    while True:
        jogadorpi = int(input('[1] Par\n[2] Ímpar\n'))
        esc_jogador = int(input('Escolhe um número entre 0 e 10: '))
        esc_maquina = randint(0,10)
        resultado = ((esc_jogador + esc_maquina) % 2)
        print(esc_maquina)
        if jogadorpi == 1:
            
            if resultado != 0:
                print(f'Você PERDEU!\nNúmero de vitórias: {contador}')
                break
            
            else:
                print(f'Você GANHOU!')
                contador += 1
        else:

            if resultado == 0:
                print(f'Você PERDEU!\nNúmero de vitórias: {contador}')
                break
            
            else:
                print(f'Você GANHOU!')
                contador += 1


ex068aa()

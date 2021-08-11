from time import sleep
import modulos115


escolha = None
while escolha != 3:
    modulos115.printMenu('MENU PRINCIPAL')
    print('1 - Ver Pessoas cadastradas\n2 - Cadastrar Pessoas\n3 - Sair do Sistema')
    print('-'*30)
    escolha = modulos115.recebeOpcao()
    modulos115.determinaOpcao(escolha)
    sleep(1.5)

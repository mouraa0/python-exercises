def printMenu(msg):
    print('-'*30)
    print(msg.center(30))
    print('-'*30)


def leiaInt(msg):
        while True:
            try:
                n = int(input(msg))
            
            except (ValueError, TypeError):
                print('ERRO! Opções estão em numerais.')
            
            else:
                return n


def cadastro():
    nome = input('Nome: ').strip()
    idade = leiaInt('Idade: ')
    return f'{nome};{idade}\n'


def recebeOpcao():
   while True:
    opcao = leiaInt('Sua opção: ')
    
    if opcao not in [1, 2, 3]:
        print('ERRO! Digite uma opção válida.')
    
    else:
        return opcao


def arquivoExiste(nome):
    try:
        f = open(nome, 'r')
    
    except:
        f = open(nome, 'a')
        f.write('Nenhuma pessoa cadastrada.')
    
    finally:
        f.close()
    

def opcao1():
    printMenu('PESSOAS CADASTRADAS')
    arquivoExiste('cadastro.txt')
    
    with open('cadastro.txt', 'r') as f:
        for l in f:
            if l == 'Nenhuma pessoa cadastrada.':
                print(l)
            else:
                info = l.replace('\n', '').split(';')
                print(f'{info[0]}, {info[1]} anos')
    

def opcao2():
    printMenu('CADASTRO')
    arquivoExiste('cadastro.txt')
    with open('cadastro.txt', 'r') as f:
        if f.readline() == 'Nenhuma pessoa cadastrada.':
            with open('cadastro.txt', 'w') as f:
                f.write(f'{cadastro()}')
        else:
            with open('cadastro.txt','a') as f:
                f.write(f'{cadastro()}')
    print('Cadastro realizado com sucesso!')


def determinaOpcao(n1):
    if n1 == 1:
        opcao1()
    
    elif n1 == 2:
        opcao2()

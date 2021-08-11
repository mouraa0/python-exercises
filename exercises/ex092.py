from datetime import datetime

def gera_cadastro():
    cadastro = dict()
    cadastro['Nome'] = input('Nome: ')
    nasc = int(input('Ano de nascimento: '))
    cadastro['Idade'] = ((datetime.now().year) - nasc)
    cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
    if cadastro['CTPS'] == 0:
        cadastro['CTPS'] = 'Não tem'
    
    else:
        cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
        cadastro['Salário'] = float(input('Salário: '))
        cadastro['Aposentadoria'] = ((cadastro['Ano de contratação'] - nasc)) + 35
    
    return cadastro

def mostra_cadastro(n1):
    for k, v in n1.items():
        print(f'{k}: {v}')


cad = gera_cadastro()
mostra_cadastro(cad)

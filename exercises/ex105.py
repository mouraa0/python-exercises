def notas(n, sit=False):
    notas_gerais = dict()
    notas_gerais['Total'] = len(n)
    notas_gerais['Maior nota'] = max(n)
    notas_gerais['Menor nota'] = min(n)
    notas_gerais['Média'] = sum(n)/len(n)

    if sit:
        if notas_gerais['Média'] >= 7:
            notas_gerais['Situação'] = 'BOA'
        
        elif notas_gerais['Média'] >= 5:
            notas_gerais['Situação'] = 'RAZOÁVEL'
        
        else:
            notas_gerais['Situação'] = 'RUIM'
    
    return notas_gerais


condicao = 'S'
n = list()

while condicao == 'S':
    n.append(float(input('Digite a nota: ')))
    condicao = input('Deseja continuar? [S/N]\n').upper()

situ = input('Deseja mostrar a situação? [S/N]\n').upper()
if situ == 'S':
    n1 = notas(n, sit=True)
else:
    n1 = notas(n)

print(n1)

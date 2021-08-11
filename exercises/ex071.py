def ex071():
    valor = int(input('Valor a ser sacado: R$'))
    nota50 = nota20 = nota10 = nota1 = 0
    
    if (valor // 50) > 0:
        nota50 += (valor//50)
        valor = valor%50
    
    if (valor // 20) > 0:
        nota20 += (valor // 20)
        valor = valor % 20
    
    if (valor // 10) > 0:
        nota10 += (valor // 10)
        valor = valor % 10
    
    if (valor // 1) > 0:
        nota1 += (valor // 1)
        valor = valor % 1
    
    totais = ('50', '20', '10', '1', nota50, nota20, nota10, nota1)
    
    for i in range(len(totais) - 4):
        if totais[i + 4] > 0:
            print(f'Notas de R${totais[i]}: {totais[i + 4]}')   
 

ex071()

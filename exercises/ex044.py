def ex044():
    valor = float(input('Preço total: R$'))
    escolha_pag = input('Escolha a forma de pagamento:\n[1] À vista dinheiro/cheque\n[2] À vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\n')
    
    if escolha_pag == '1' or escolha_pag == '2':
        if escolha_pag == '1':
            desconto = (10/100)
        else:
            desconto = (5/100)
        valor_final = (valor - (valor*desconto))
    elif escolha_pag == '3':
        valor_final = valor
    else:
        juros = (20/100)
        valor_final = (valor + (valor*juros))
    
    print(f'Preço final: R${valor_final:.2f}')

ex044()

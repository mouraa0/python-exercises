def ex036():
    valor = float(input('Valor da casa: R$'))
    salario = float(input('Seu salário: R$'))
    anos = float(input('Quantos anos de financiamento: '))
    
    if valor/(anos*12) <= salario*(30/100):
        print('Pedido Aceito!')
    else:
        print('Pedido Negado!') 


ex036()

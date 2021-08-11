def ex034():
    salario = float(input('Digite o salário: R$'))
    diferencial = 1250

    if salario <= diferencial:
        aumento = (115/100)
    else:
        aumento = (110/100)
    
    print(f'Novo salário: R${(salario*aumento):.2f}')


ex034()

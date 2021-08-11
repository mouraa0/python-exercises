def ex083():
    expressao = input('Digite a expressão:\n')
    paren_a = 0
    paren_f = 0
    
    for i in expressao:
        if i == '(':
            paren_a += 1
        elif i == ')':
            paren_f += 1
    
    if paren_a == paren_f:
        resultado = 'VÁLIDA'
    else:
        resultado = 'INVÁLIDA'
    
    print(f'A equação digitada é {resultado}')


ex083()

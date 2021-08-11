def _leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
        
        else:
            return n

def _leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        
        except (ValueError, TypeError):
            print('Erro! Digite um número real válido.')
        
        else:
            return n


num_int = _leiaInt('Digite um número inteiro: ')
num_float = _leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi: {num_int}\nO número real digitado foi: {num_float}')

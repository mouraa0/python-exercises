def voto(ano):
    from datetime import date
    
    idade = (date.today().year) - ano
    if idade < 16:
        return idade, 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return idade, 'VOTO OPCIONAL'
    else:
        return idade, 'VOTO OBRIGATÓRIO'


nasc = int(input('Digite o ano de nacimento: '))
print(f'Com {voto(nasc)[0]} anos: {voto(nasc)[1]}')

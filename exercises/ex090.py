def ex090():
    aluno = dict()
    aluno['nome'] = input('Nome do aluno: ')
    aluno ['media'] = float(input('Média do aluno: '))
    
    if aluno['media'] >= 6:
        aluno['situacao'] = 'Aprovado'
    
    else:
        aluno['situacao'] = 'Reprovado'
    
    print(f'Nome: {aluno["nome"]}\nMédia: {aluno["media"]}\nSituação: {aluno["situacao"]}')


ex090()

def ex061():
    primeiro_termo = int(input('Primeiro termo da PA: '))
    razao = int(input('Razão da PA: '))
    print(primeiro_termo)
    for i in range(1, 10):
        print(primeiro_termo + razao)
        primeiro_termo += razao
    

ex061()

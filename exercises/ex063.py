#0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21
def ex062():
    qtd = int(input('Quantos números? '))
    prim = 0
    seg = 1
    print(f'{prim}\n{seg}')
    for i in range(1, (qtd - 1)):
        print(prim+seg)
        temp = prim
        prim = seg
        seg = temp + seg

ex062()

from random import randint
from operator import itemgetter

def ex091():
    results = {'jogador1':0,
             'jogador2':0,
             'jogador3':0,
             'jogador4':0,}         
                          
    for i in results:
        results[i] = randint(1,6)
    
    for k, v in results.items():
        print(f'O {k} tirou {v}')
    
    ranking = sorted(results.items(), key=itemgetter(1), reverse=True)
    
    print('='*30)
    for k, v in enumerate(ranking):
        print(f'{k + 1}º lugar: {v[0]} tirou {v[1]}.')


ex091()

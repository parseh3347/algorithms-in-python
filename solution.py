from collections import Counter
def fruits():

    output =  ((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))

    dict={}

    for i in output:
        if ((i['shape']=='sphere')
             and (300<= i['mass'] <=600)
             and (100<= i['volume'] <= 500)) :
            
            dict.setdefault(i['mass'],i['name'])
            print(i)

    print('-'*65)
    print(Counter((dict.values())),'\n')


fruits()
def find(x,y,z):
    x,y,z =map(int,input('enter tree number with seprator "," : ').split(','))

    if (x==y or x==z or y==z):
        print(f'numbers is reduplicative x:{x} y:{y} z:{z}' )
    elif (x>4 or x>4 or z>4):
        print(f'numbers must among 1 till 4  x:{x} y:{y} z:{z}' )

    else:
        f=10
        sum=(x+y+z)
        print('result:',f-sum)

find(1,2,3)

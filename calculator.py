def calculate_floor(string):

    floor=0
    # string = input('enter your choice four between D(Downstairs) and U(Upstairs :) ').upper()
    
    if len(string)!=4:
        print('length string must 4')
    else:
        for i in string:
            if i == 'D':
                floor-=1
            elif i== 'U':
                floor+=1
        return floor
        
# print(calculate_floor('uudu'))

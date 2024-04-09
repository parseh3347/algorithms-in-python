def insertionsort(l: list):
    if any(not isinstance(x,int) or x<0 for x in l):
        raise TypeError('arguman must be list of non-nagative integer')
    
    for i in range(1, len(l)):
        cv = l[i]

        while i > 0 and l[i-1] > cv:
            l[i] = l[i-1]
            i = i-1
        l[i] = cv
        
a=[4,1,5,3,8,41,7,11,0]
insertionsort(a)
print(a)

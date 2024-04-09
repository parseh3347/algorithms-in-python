def bubblesort(l:list):
    if any(not isinstance(x,int) or x<0 for x in l):
        raise TypeError('argumon must be list of non-nagative integer')
    
    for i in range(0,len(l)-1):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
                    
print(bubblesort([5,2,3,4,1,9]))
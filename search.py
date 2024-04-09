def search(l:list,query):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(high+low)//2
        val = l[mid]
        if val==query:     
            return mid
        elif val<query:    
            low=mid+1
        else:
            high=mid-1
    else:
        print('not found')
    return mid

print(search([1,4,6,7,9,15],11))
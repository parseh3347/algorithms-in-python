def zig_zag(l,l1):
    list=[]
    i=len(l)
    j=len(l1)
    m=max(i,j)
    print(m)
    for x in range(m):
        list.append(l[x])
        list.append(l1[x])
        
    return list

print(zig_zag([1,3,5,7],[2,4,6,8,10]))
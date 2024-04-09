def selectionsort(l: list):
    for i in range(len(l)-1,0,-1):
        p=0
        for j in range(1,i+1):
            if l[j]>l[p]:
                p=j
        l[i],l[p]=l[p],l[i]

a=[4,1,5,3,8,41,7,11,0]
selectionsort(a)
print(a)

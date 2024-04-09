def calculator(n, m, li):
    n = len(li)
    s=[]
    s1=[]
    s2=[]
    x=li[0]
    p=0
    for i in range(0,n,m):
        y=i+m
        p=0
        if y>n:
            y=n
        for j in range(i,y):
            p+=li[j]
            s.append(li[j])
        s1.append(s)
        s2.append(p)
        s=[]
    print(s1)
    print(s2)
    print('-'*55)
    for v in range(1,len(li)):
        if not v % 2==0:
            x += li[v]
        else:
            x -= li[v]
    print(x, end=' ')

calculator(n=8, m=3, li=[1,2,3,4,5,6,7,8]) 
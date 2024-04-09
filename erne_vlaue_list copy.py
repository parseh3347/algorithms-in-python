from itertools import islice
from functools import partial

def take_calc(l,m):
    return list(islice(l,m))

def chunked(li,n,strict=False):
    l=list(iter(partial(take_calc, iter(li),n),[]))
    return l

def sum_calc(l):
    su_c=[sum(i) for i in l]
    return su_c

def sum_total(l):
    xx=l[0]

    for i in range(1,len(l)):
        if not i % 2 == 0:
            xx -= l[i]
        else:
            xx += l[i]
    return xx

c=[1,2,3,4,5,6,7,8]

ch = chunked(c,3)
print(ch)

su_c=sum_calc(ch)
print(su_c)

su_t=sum_total(su_c)
print(su_t)
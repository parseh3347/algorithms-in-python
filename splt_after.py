def split_after(iterable,period,split_max=-1):
    if split_max==0:
        yield list(iterable)
        return 
    
    buf=[]
    it=iter(iterable)
    for item in it:
        buf.append(item)
        if period(item) and buf:
            yield buf
            if split_max==1:
                yield list(it)
                return
            buf=[]
            split_max -=1
    if buf:
        yield buf
    # return buf



l=[0,0,1,1,2,3,4,5,6,8,9,9,9]

# a=list(split_after(l,[i for i in l if i%3==0]))
b=list(split_after(l,lambda c: c%3==0))
# print(a)
print(b)

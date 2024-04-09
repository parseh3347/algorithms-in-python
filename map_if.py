def map_if(iterable,pred,func,func_else=lambda x:x):
    for i in iterable:
        yield func(i) if pred(i) else func_else(i)


a=map_if([1,2,3],lambda x: x>2 , lambda x:'hello')

print(list(a))

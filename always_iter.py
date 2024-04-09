def always_iterable(obj,base_type=(str,bytes)):
    if obj is None:
        return iter(())
    
    if (base_type is not None) and isinstance(obj,base_type):
        return iter((obj,))
    
    try:
        return iter(obj)
    except TypeError:
        return iter((obj,))
    

a=always_iterable({'s':12,'r':465,10:['sdfg']})
print(list(a))


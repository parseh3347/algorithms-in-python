def alwasy_revarsable(iterable):
    try :
        return reversed(iterable)
    except TypeError:
        return reversed(list(iterable))
    

a=alwasy_revarsable(range(10))
print(list(a))
from itertools import islice
def split_into(iterable,size):
    it = iter(iterable)

    for s in size:
        if s is None:
            yield list(it)
            return
        else:
            yield list(islice(it,s))

into=list(split_into([1,2,3,4,5,6,7,8,'a','b','c','f'],[2,3,None]))
print(into)
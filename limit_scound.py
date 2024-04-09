from time import monotonic
class limmit_second:
    def __init__(self,limit_second,iterable) :
        if limit_second<0 :
            raise ValueError('limit sconde must postive')
        self.limit_second=limit_second
        self._iterable=iter(iterable)
        self._start_time=monotonic()
        self.time_out=False

    def __iter__(self):
        return self

    def __next__(self):
        item=next(self._iterable)
        if monotonic()-self._start_time > self.limit_second:
            self.time_out=True
            raise StopIteration
        return item
    

c=list(limmit_second(0.000000000001,range(1,100)))
print(c)
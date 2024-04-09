from functools import partial
from itertools import islice

class Reprator:
    def __init__(self, value,max_v):
        self.value=value
        self.max_v=max_v
        self.count=0

  
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count>=self.max_v:
            raise StopIteration
        else:
            self.count +=1

        return self.value
    
r=Reprator('hello',5)
print(next(r))
for i in r:
    print(i)
   

import collections
from typing import NamedTuple
import heapq

class Car(NamedTuple):
    color: str
    mileage : int
    price : float

    def heap1(self):
        q=[]
        heapq.heappush(q,(2,'name'))
        heapq.heappush(q,(3,'family'))
        heapq.heappush(q,(1,'code'))
        print(q)
        # return q

    # def next_item(self):
    #     while self.heap1():
    #         n=heapq.heappop(self.heap1())
    #         print(n)

car1=Car('red',3812.1,125500)
print(car1)

# car2=Car()
car1.heap1()
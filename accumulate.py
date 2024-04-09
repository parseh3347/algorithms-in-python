import operator
from functools import reduce
from itertools import accumulate

l=[18,7,22,6,4]

print(reduce(operator.add,l))

print(list(accumulate(l,func=operator.sub)))


# for i in range(len(l)-1):
#     s=l[i]-l[i+1]
#     print(s)
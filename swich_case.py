def s(p,x,y):
    if p=='add':
        return x+y
    elif p=='mul':
        return x*y
    elif p=='sub':
        return x-y
    elif p=='div':
        return x/y


def u(p,x,y):
    return{
        'add':lambda: x+y,
        'sub':lambda: x-y,
        'mul':lambda: x*y,
        'div':lambda: x/y,
    }.get(p,input())()

print(u('div',5,3))
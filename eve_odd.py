def separator(ls):
    tuple=()
    even,odd=[],[]
    for i in ls:
        if i % 2==0:
            even.append(i)
        else:
            odd.append(i)
    tuple=(even,odd)
    return tuple

print(separator([-3, -2, -1, 0, 1, 2, 3]))
def max_repet(arr):
    value={}
    result={}
    f_val=0
    
    for i in arr:
        if i in value: 
            value[i]+=1
        else:
            value[i]=1
    f_val=max(value.values())

    for j in value:
        if value[j]==f_val:
            result.setdefault(j, value[j])
        
    print(value)
    print(f'most repat {f_val} and index is = {result}')


max_repet([1,2,3,4,4,4,5,5,5,6,22])
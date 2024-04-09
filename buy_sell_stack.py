def max_profit(l:list):
    cur_max,val_max=0,0
    for i in range(1,len(l)):
        cur_max = max(0,cur_max+l[i]-l[i-1]) # -4,0 2 6 -2 7
        val_max = max(cur_max,val_max) # 0,0 0,2 2,6 6,-2 6
    return f'max:{val_max} and  index:{i} value:{l[i]}'

print(max_profit([7,3,5,9,1,3,8]))
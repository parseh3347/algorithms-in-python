def limit(arr,min=None,max=None):
    arr_min=lambda val:True if min is None else (min >= val)
    arr_max=lambda val:True if max is None else (max <= val)

    return [val for val in arr if arr_min(val) and arr_max(val)]

print(limit([1,2,3,4,5,6],max=5))
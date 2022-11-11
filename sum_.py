def sum_array(arr):
    import math
    arr = []
    if arr:
        m = math.max(arr)
        l = math.min(arr)
        
        return m + l

arr = [1,2,3,5]
print(sum_array(arr))
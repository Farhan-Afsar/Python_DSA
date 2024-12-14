def binarySearch(arr,target):
    n = len(arr)
    l = 0
    r = n - 1

    while l <= r:
        m = l + ((r-l) // 2)

        if arr[m] == target:
            return True
        elif target < arr[m] :
            r = m - 1
        else:
            l = m + 1
    
    return False

a = [1,3,45,65,78]
print(binarySearch(a,65))

def binaryCondition(arr):
    n = len(arr)
    l = 0
    r = n - 1

    while l < r:
        m = l + ((r-l) // 2)

        if arr[m]:
            r = m
        else:
            l = m + 1
    
    return l
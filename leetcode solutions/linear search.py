def linear_search(arr,target):
    for num in arr:
        if num == target:
            return True
    return False

arr = [9,3,5,1,4]
target = 2
print(linear_search(arr,target))
"""This is the better way to search a number in a array
   prerequisite to perform binary search is the array should be sorted"""

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    arr.sort()
    while(left <= right):
        mid = (left+right)// 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return False


arr = [9,76,4,6,1,2,7]
target = 76
print(binary_search(arr,target))
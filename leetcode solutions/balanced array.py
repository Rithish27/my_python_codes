"""We should return the index at which the sum of all left elements 
   is equal to sum of all right elements"""

def balanced_array(arr):
    leftSum , rightSum = 0, sum(arr)

    for ind,ele in enumerate(arr):
        rightSum -= ele
        if leftSum == rightSum:
            return ind
        leftSum += ele
    return -1

arr = [1,2,3,4,6]
print(balanced_array(arr))
""" This is a program to find a number in the given array of numbers
    return true if the given number exists in the array else false"""


def linear_search(arr,target):
    for num in arr:
        if num == target:
            return True
    return False

arr = [9,3,5,1,4]
target = 2
print(linear_search(arr,target))
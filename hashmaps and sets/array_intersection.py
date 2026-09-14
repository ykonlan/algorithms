""" Write a function that returns the intersection of two arrays. The intersec
tion is a third array that contains all values contained within the first two
arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
Your function should have a complexity of O(N). (If your programming
language has a built-in way of doing this, don’t use it. The idea is to build
the algorithm yourself. """

def array_intersection(arr1:list, arr2:list):
    arr1_size = len(arr1)
    arr2_size = len(arr2)
    if (arr1_size > arr2_size):
        lookup_set = set(arr1)
        other = arr2
    else:
        lookup_set = set(arr2)
        other = arr1
    return [member for member in other if member in lookup_set]

ans = array_intersection([1, 2, 3, 4, 5],[0, 2, 4, 6, 8])
print(ans)

    
            
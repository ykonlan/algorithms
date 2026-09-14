def selection_sort(nums:list):
    the_size = len(nums)
    if the_size == 1:
        return nums
    for i in range(the_size-1):
        temp = i
        swapped = False
        for j in range(i+1, the_size):
            if nums[j] < nums[temp]:
                temp = j
                swapped = True
        if not swapped:
            return nums
        nums[i], nums[temp] = nums[temp], nums[i]
    return nums

ans = selection_sort([5,4,3,2,1])
print(ans)


    

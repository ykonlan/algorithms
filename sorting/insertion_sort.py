def insertion_sort(nums:list):
    the_size = len(nums)
    if the_size == 1:
        return nums
    for i in range(1, the_size):
        temp = nums[i]
        prev = i - 1
        while prev >= 0:
            if temp < nums[prev]:
                nums[prev + 1] = nums[prev] 
                prev -= 1
            else:
                break
        nums[prev + 1] = temp
    return nums

ans = insertion_sort([5,4,3,2,1])
print(ans)


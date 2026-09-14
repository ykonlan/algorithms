def bubble_sort(nums):
    if len(nums) <= 1:
        return nums
    sorted_from = len(nums)
    for i in range(len(nums)):
        left = 0
        right = left + 1
        swapped = False
        while right < sorted_from:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                swapped = True
            left += 1
            right += 1
        sorted_from -= 1
        if not swapped:
            break
    return nums


ans = bubble_sort([5,4,3,2,1])
print(ans)
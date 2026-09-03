def two_sum(nums, target):
    if not isinstance(nums, list) or not isinstance(target, int):
        raise TypeError("nums must be a list and target must be an integer")
    seen = {}
    for i in range(len(nums)):
        if (target - nums[i]) not in seen:
            seen[nums[i]] = i
        else:
            return [seen[(target - nums[i])], i]

ans = two_sum([1,2,4], 6)
print(ans)
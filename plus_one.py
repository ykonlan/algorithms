def plus_one(digits:list):
    for i in range(len(digits))[::-1]:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

ans = plus_one([1,2,3])
print(ans)


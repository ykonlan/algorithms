def fiboncacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fiboncacci(n-1) + fiboncacci(n-2)

# print(fiboncacci(4))

# implementing fiboncacci iteratively
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    prev, prevv = 0, 1
    current = 1
    for i in range(3, n):
        prev = prevv
        prevv = current
        current = prev + prevv
    return current

print(fib(9))

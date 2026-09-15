""" Given a string, return true if the given string is a palindrome and false if it is not """

# RECURSIVE VERSION
def is_palindrome(string:str):

    def helper(left, right):
        if string[left] != string[right]:
            return False
        while left < right:
            return helper(left + 1, right - 1)
        return True
    return helper(0, len(string)-1)


# ITERATIVE VERSION
def is_palindrome_it(string:str):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome_it("racecar"))

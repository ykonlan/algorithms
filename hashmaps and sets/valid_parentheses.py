""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. """

def valid_parentheses(string:str):
    reference = {"{":"}",
                 "[":"]",
                 "(":")"}
    stack = []
    for char in string:
        if char in reference:
            stack.append(char)
        else:
            if not stack:
                return False
            popped = stack.pop()
            if char != reference[popped]:
                return False
    return not stack

ans = valid_parentheses("([)]")
print(ans)

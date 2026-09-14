""" Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist
once—the "n" and the "u", so your function should return the "n", since it
occurs first. The function should have an efficiency of O(N) """

def first_non_duplicate(string:str):
    seen = set()
    non_duplicate = None
    for i in range(len(string)-1, -1, -1):
        if string[i] not in seen:
            seen.add(string[i])
            non_duplicate = string[i]
    return non_duplicate

ans = first_non_duplicate("minimum")
print(ans)

""" Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. For example, the string,
"the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
except the letter, "f". The function should have a time complexity of O(N) """

def missing_letter(sentence:str):
    seen = set(sentence)
    for i in range(97,123):
        if chr(i) not in seen:
            return chr(i)

ans = missing_letter("the quick brown box jumps over a lazy dog")
print(ans)
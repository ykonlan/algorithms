""" write a function that returns an array of all anagrams of a
given string """

def anagram_generation(string:str):
    return generate("", string)



def generate(current, remaining):
    anagrams = []
    if not remaining:
        anagrams.append(current)
        return anagrams
    for i in range(len(remaining)):
        old_current, old_remaining = current, remaining
        current += remaining[i]
        remaining = remaining[0:i] + remaining[i+1:]
        anagrams += generate(current, remaining)
        current, remaining = old_current, old_remaining
    return anagrams

print(anagram_generation("abc"))

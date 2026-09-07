def missing_letter(sentence:str):
    seen = set(sentence)
    for i in range(97,123):
        if chr(i) not in seen:
            return chr(i)

ans = missing_letter("the quick brown box jumps over a lazy dog")
print(ans)
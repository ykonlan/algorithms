""" Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000 """

def romanToInt(s: str) -> int:
    ref = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    sum = 0
    i = 0
    while i < (len(s) - 1):
        if ref[s[i]] < ref[s[i + 1]]:
            sum -= ref[s[i]]
        else:
            sum += ref[s[i]]
        i += 1
    sum += ref[s[i]]
    return sum

    
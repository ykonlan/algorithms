def is_palindromic_number(number:int):
    samp = number
    number2 = 0
    while samp > 0:
        number2 = (number2 * 10) + samp % 10
        samp //= 10
    return number == number2

print(is_palindromic_number(102))
     


def countdown(num:int):
    if num < 0:
        return
    print(num)
    countdown(num-1)

countdown(10)
""" Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead. """

def dailyTemperatures(temperatures: list[int]):
        output = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack and (temperatures[i] > temperatures[stack[-1]]):
                    popped = stack.pop()
                    output[popped] = i - popped
                stack.append(i)
        return output

ans = dailyTemperatures([73,74,75,71,69,72,76,73])
print(ans)
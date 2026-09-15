def subset_generator(array:list):
    result = []


    def generator(current, index):
        if index == len(array):
            result.append(current.copy())
            return result
        for i in range(len(array)):
            current.append(array[i])
            generator(current, index + 1)
            current.pop()
            generator(current, index + 1)
        return result

    return generator(array, 0)

print(subset_generator([1,2,3]))






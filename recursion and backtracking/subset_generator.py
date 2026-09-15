""" Given a list of integers, generate all ppossible subsets of the set """

def subset_generator(array:list):
    result = []


    def generator(current, index):
        if index == len(array):
            result.append(current.copy())
            return
        current.append(array[index])
        generator(current, index + 1)
        current.pop()
        generator(current, index + 1)
        return result

    return generator([], 0)

print(subset_generator([1,2,3]))






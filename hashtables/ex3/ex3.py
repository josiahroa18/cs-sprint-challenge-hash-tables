def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for x in range(len(arrays)):
        for y in range(len(arrays[x])):
            if arrays[x][y] in cache:
                cache[arrays[x][y]] += 1
            else:
                cache[arrays[x][y]] = 1
            if cache[arrays[x][y]] == len(arrays):
                result.append(arrays[x][y])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

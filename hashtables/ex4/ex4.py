def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for num in a:
        if num not in cache:
            num = num * -1
            cache[num] = True
        else:
            if num < 0:
                num = num * -1
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

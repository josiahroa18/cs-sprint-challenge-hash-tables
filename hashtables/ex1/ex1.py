def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Store key=weight, value=index in a hashtable
    cache = {}
    for i in range(len(weights)):
        cache[weights[i]] = i

    # CHECK: Subtract each weight from limit
    for i in range(len(weights)):
        possible_value = limit - weights[i]
        if possible_value in cache:
            return [cache[possible_value], i]

    return None

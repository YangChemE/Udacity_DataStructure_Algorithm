#### Naive approach based on Recursion (exponential time) ###
def knapsack_max_value(knapsack_max_weight, items):
    lastIndex = len(items) - 1
    return knapsack_recursive(knapsack_max_weight, items, lastIndex)


def knapsack_recursive(capacity, items, lastIndex):
    # Base case
    if (capacity <= 0) or (lastIndex<0):
        return 0
    
    # Put the item in the knapsack
    valueA = 0
    if (items[lastIndex].weight <= capacity):
        valueA = items[lastIndex].value + knapsack_recursive(capacity - items[lastIndex].weight, items, lastIndex - 1)

    
    # Do not put the item in the knapsack
    valueB = knapsack_recursive(capacity, items, lastIndex - 1)
    
    # Pick the maximum of the two results
    result = max(valueA, valueB)
    
    return result


#### DP approach ###
def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    capacity = knapsack_max_weight
    lookup_table = [0 for _ in range (knapsack_max_weight + 1)]
    for item in items:
        
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                value_A = lookup_table[capacity]
        
                value_B = lookup_table[capacity - item.weight] + item.value
                lookup_table[capacity] = max(value_A, value_B)

    
    return lookup_table[-1]

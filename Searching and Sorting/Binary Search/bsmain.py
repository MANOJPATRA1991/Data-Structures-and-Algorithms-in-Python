
def binary_search(input_array, value):
    """
    Binary search
    Args:
        input_array: List in which to search
        value: Item to search for
    Returns:
        Integer: Index of the element if found else -1
    """
    # Keeps track of start index
    first = 0
    # Keeps track of end index
    last = len(input_array) - 1
    
    while first <= last:
        # Find the mid value
        mid = (first + last)//2
        # If item is the mid value of the list
        if input_array[mid] == value:
            return input_array.index(value)
        # If item is greater than the mid value,
        # search in the right half
        elif value > input_array[mid]:
            first = mid + 1
        # If item is less than the mid value,
        # search in the left half
        elif value < input_array[mid]:
            last = mid - 1
            
    # Item not found
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))

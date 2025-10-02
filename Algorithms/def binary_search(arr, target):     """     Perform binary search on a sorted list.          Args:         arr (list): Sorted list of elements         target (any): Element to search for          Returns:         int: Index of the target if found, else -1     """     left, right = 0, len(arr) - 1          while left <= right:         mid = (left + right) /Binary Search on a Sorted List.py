def binary_search(arr, target):
    """
    Perform binary search on a sorted list.
    
    Args:
        arr (list): Sorted list of elements
        target (any): Element to search for
    
    Returns:
        int: Index of the target if found, else -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# Example usage
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    index = binary_search(numbers, target)
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found.")

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid # target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 # target not found


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return - 1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target,low, mid - 1)
    
    
    
# Example usage
if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10, 12, 14, 16]
    
    target = 10
    print(f"\nThe Number list is: {numbers}")
    print(f"\nTarget is {target}")
    result_iterative = binary_search_iterative(numbers , target)
    print(f"\nIterative: Found Target at index {result_iterative}")
    
    result_recursive = binary_search_recursive(numbers, target, 0 , len(numbers) - 1)
    print(f"\nRecursive: Found {target} at index {result_recursive}")
def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)

    return -1  # Element not found

# Example usage
sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56]
target_element = 23
result = binary_search_recursive(sorted_array, target_element, 0, len(sorted_array) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array.")

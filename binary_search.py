def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    :param arr: List of sorted elements
    :param target: Element to search for
    :return: Index of the target element if found, otherwise -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid potential overflow

        # Check if the target is at the mid index
        if arr[mid] == target:
            return mid
        # If the target is smaller, ignore the right half
        elif arr[mid] > target:
            right = mid - 1
        # If the target is larger, ignore the left half
        else:
            left = mid + 1

    # Target not found
    return -1


# Example usage
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13]
    target_value = 7

    result = binary_search(sorted_array, target_value)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

        
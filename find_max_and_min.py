def find_max_and_min(numbers: list) -> tuple:
    largest = second_largest = float('-inf')  # '-inf' represents the smallest possible value
    smallest = second_smallest = float('inf')  # 'inf' represents the largest possible value

    for num in numbers:
        # Updating the largest number
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

        # Updating the smallest number
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return largest, smallest  # Returning the largest and smallest values

# Example usage
numbers = [99, 12, 53, 2, 10, 1, 53, 12, 13]
print(find_max_and_min(numbers))  # Output: (53, 1)

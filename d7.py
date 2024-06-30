def find_target(nums, target):
    for i, num in nums:
        if num == target:
            return i
    return -1

# Examples
print(find_target([4, 2, 1, 7, 3], 7))  # Output: 3
print(find_target([4, 2, 1, 7, 3], 5))  # Output: -1

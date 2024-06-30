def contains_duplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# Examples
print(contains_duplicate([1, 2, 3, 1]))  # Output: True
print(contains_duplicate([1, 2, 3, 4]))  # Output: False

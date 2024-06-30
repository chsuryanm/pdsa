def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

# Example
print(insertion_sort([3, 1, 2, 5, 4]))  # Output: [1, 2, 3, 4, 5]

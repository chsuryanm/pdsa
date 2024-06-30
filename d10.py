def permute(nums):
    result = []
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    
    for i in range(len(nums)):
        m = nums[i]
        remaining_list = nums[:i] + nums[i+1:]
        for p in permute(remaining_list):
            result.append([m] + p)
    return result

# Example
print(permute([1, 2, 3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

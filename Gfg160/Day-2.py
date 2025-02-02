# Python Program to move all zeros to the end
def moveZeroes(nums):
    count = 0  # Position for the next non-zero element

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[count] = nums[count], nums[i]  # Swap
            count += 1  # Move pointer forward

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

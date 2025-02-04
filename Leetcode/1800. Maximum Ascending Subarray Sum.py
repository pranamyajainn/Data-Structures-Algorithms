from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case: If only one element, return it
        if n == 1:
            return nums[0]

        # Initialize sum variables
        max_sum = nums[0]  # Stores max ascending sum
        current_sum = nums[0]  # Sum of current ascending subarray

        for i in range(1, n):  # Start from index 1 to avoid IndexError
            if nums[i] > nums[i - 1]:  # Check if increasing
                current_sum += nums[i]
            else:  # If not increasing, reset
                max_sum = max(max_sum, current_sum)  # Update max sum
                current_sum = nums[i]  # Start a new subarray sum

        # One last check to update max_sum after loop
        max_sum = max(max_sum, current_sum)
        
        return max_sum

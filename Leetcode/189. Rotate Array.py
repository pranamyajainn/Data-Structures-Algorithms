class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Ensure k is within bounds

        if n == 1 or k == 0:  # Handle edge cases
            return

        temp = [0] * n

        # Copy the last k elements to temp
        for i in range(k):
            temp[i] = nums[n - k + i]

        # Copy the first n-k elements (shift them right)
        for i in range(n - k):
            temp[k + i] = nums[i]

        # Copy back to nums
        for i in range(n):
            nums[i] = temp[i]

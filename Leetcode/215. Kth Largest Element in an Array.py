from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # Convert k-th largest to index
        
        def quickSelect(left, right):
            pivot = nums[right]  # Choose pivot (last element)
            p = left  # Partition index
            
            # Partitioning: Place elements <= pivot on left
            for i in range(left, right):
                if nums[i] <= pivot:  # Swap only if nums[i] is smaller than or equal to pivot
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            # Place pivot at its correct position
            nums[p], nums[right] = nums[right], nums[p]
            
            # Recursively search in the correct partition
            if p < k:
                return quickSelect(p + 1, right)  # Search right half
            elif p > k:
                return quickSelect(left, p - 1)  # Search left half
            else:
                return nums[p]  # Found the k-th largest element
        
        return quickSelect(0, len(nums) - 1)

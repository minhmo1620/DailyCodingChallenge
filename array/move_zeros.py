# Link: https://leetcode.com/problems/move-zeroes/
# This solution is based on swapping between 0 and another non-zero number
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        
        while j < len(nums):
            if nums[i] == 0:
                if nums[j] != 0 and i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            else:
                i += 1
            
            j += 1

#link:https://leetcode.com/problems/array-partition-i/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range (len(nums)):
            if i % 2 == 0:
                cnt += nums[i]
        return cnt

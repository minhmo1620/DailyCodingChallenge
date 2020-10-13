# Link: https://leetcode.com/problems/single-number/
# There are several ways to solve this problem, personally I think using dictionary is an easy but boring solution
# We can solve in O(1) by Math and set()

# Solution 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            
        for key, value in d.items():
            if value == 1:
                return key

# Solution 2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set(nums)
        return 2*sum(s) - sum(nums)

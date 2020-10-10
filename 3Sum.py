class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2):
            R = len(nums) - 1
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            while L < R:
                s = (nums[i] + nums[L] + nums[R])
                if s == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    R -= 1
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                elif s > 0:
                    R -= 1
                else:
                    L += 1
        return res

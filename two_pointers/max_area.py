# Link: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1

        res = 0
        while L < R:
            area = min(height[L], height[R]) * (R - L)
            res = max(res, area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return res

#link:https://leetcode.com/problems/height-checker/
#time: 28ms
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        
        cnt = 0
        for i in range (len(heights)):
            if heights[i] != s[i]:
                cnt += 1
        return cnt

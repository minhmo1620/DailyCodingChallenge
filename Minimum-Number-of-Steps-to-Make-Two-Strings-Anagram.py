#link:https://leetcode.com/contest/weekly-contest-175/problems/minimum-number-of-steps-to-make-two-strings-anagram/
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = [0] * 26
        for i in s:
            d[ord(i) - ord("a")] += 1
        
        x = [0] * 26
        for i in t:
            x[ord(i) - ord("a")] += 1
        
        cnt = 0
        for i in range (len(x)):
            cnt += abs(x[i] - d[i])
        return cnt//2

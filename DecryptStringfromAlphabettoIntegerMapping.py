#link:https://leetcode.com/contest/weekly-contest-170/problems/decrypt-string-from-alphabet-to-integer-mapping/
class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = dict()
        x = "abcdefghijklmnopqrstuvwxyz"
        curr = 0
        ans = ""
        while curr < len(s):
            tmp = ""
            if curr+2 < len(s) and s[curr+2] == "#":
                ans += x[int(s[curr:curr+2]) -1]
                curr += 3
            else:
                ans += x[int(s[curr]) - 1]
                curr += 1
        return ans

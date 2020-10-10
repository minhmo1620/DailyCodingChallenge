#Longest Substring with At Most Two Distinct Characters
#codeInterview link: https://codeinterview.io/NATPLDCPEW
#source: Gấu 
class Solution:
    def getCh(self, ch):
        if 'a' <= ch <= 'z':
          return ord(ch) - ord('a')
        else:
          return ord(ch) - ord('A') + 26
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        cnt = [0] * 52 
        diff = 0 
        res = 0
        L = 0
        for R in range(len(s)):
          if cnt[self.getCh(s[R])] == 0: 
            diff += 1
          cnt[self.getCh(s[R])] += 1
          while diff > 2:
            if cnt[self.getCh(s[L])] == 1: 
              diff -= 1
            cnt[self.getCh(s[L])] -= 1
            L += 1

          res = max(res, R - L + 1)
        return res

#link:https://leetcode.com/problems/reverse-string-ii/
#93.02% time, 100% space
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        cnt = 0
        
        res = ''
        while len(s) - cnt > 0:
            if (len(s) - cnt) < k:
                res += s[cnt:][::-1]
                return res
            elif k <= len(s) - cnt < 2 *k:
                res += s[cnt:(cnt+k)][::-1]
                res += s[(cnt+k):]
                cnt += 2*k
            else:
                res += s[cnt:(cnt+k)][::-1]
                res += s[(cnt+k):(cnt+2*k)]
                cnt += 2*k
        return res
                

#link: https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        L = 0
        
        res = []
        
        while L < len(S):
            cnt = 0
            for R in range (L, len(S)):
                if S[R] == S[L]:
                    cnt += 1
                else:
                    break
            if cnt >= 3:
                res.append([L, L + cnt - 1])
            L = R
            if R == len(S) - 1:
                break
        return res
            

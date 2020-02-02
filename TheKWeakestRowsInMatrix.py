#link:https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
#time: beat 100%
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        num = []
        for i in range (len(mat)):
            num.append([i, sum(mat[i])])
        num.sort(key=lambda x:x[1])
        
        for i in range (k):
            ans.append(num[i][0])
        return ans

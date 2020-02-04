#link: https://leetcode.com/contest/biweekly-contest-18/problems/rank-transform-of-an-array/
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = dict()
        x = arr[:]
        x.sort()
        for i in range (len(x)):
            if x[i] not in d:
                d[x[i]] = len(d)
        res = []
        for i in arr:
            res.append(d[i] + 1)
        return res
        

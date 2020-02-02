#link: https://leetcode.com/problems/reduce-array-size-to-the-half/
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = dict()
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        x = list(sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse = True))
        
        cnt = 0
        limit = len(arr)//2
        i = 0
        
        while cnt < limit:
            cnt += x[i][1]
            i += 1
        return i

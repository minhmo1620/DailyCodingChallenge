#link: https://leetcode.com/contest/weekly-contest-175/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = dict()
        for i in (arr):
            if i in d:
                return True
            else:
                if i % 2 == 0:
                    d[i//2] = 1
                d[i*2] = 1
        return False
            

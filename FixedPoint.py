#link:https://leetcode.com/problems/fixed-point/
#time: 60ms, beat 95%
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i in range (len(A)):
            if i == A[i]:
                return i
        return -1

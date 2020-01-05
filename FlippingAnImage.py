#link: https://leetcode.com/problems/flipping-an-image/
#running time: 44ms, beat 93%
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range (len(A)):
            A[i] = A[i][::-1]
            for j in range (len(A[i])):
                A[i][j] = abs(1-A[i][j])
        return A

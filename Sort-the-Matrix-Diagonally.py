#link:https://leetcode.com/problems/sort-the-matrix-diagonally/
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range (len(mat)):
            ans.append([None]*len(mat[i]))
        for i in range (len(mat)):
            row = i
            col = 0
            temp = []
            while row < len(mat) and col < len(mat[0]):
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row = i
            col = 0
            p = 0
            for k in range (len(temp)):
                ans[row][col] = temp[k]
                row += 1
                col += 1
        for i in range (1, len(mat[0])):
            row = 0
            col = i
            temp = []
            while row < len(mat) and col < len(mat[0]):
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row = 0
            col = i
            for k in range (len(temp)):
                ans[row][col] = temp[k]
                row += 1
                col += 1
        return ans

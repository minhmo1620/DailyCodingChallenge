#link: https://leetcode.com/contest/weekly-contest-176/problems/count-negative-numbers-in-a-sorted-matrix/
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in grid:
            for j in i:
                if j < 0:
                    cnt += 1
                    
        return cnt

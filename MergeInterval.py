#link:https://leetcode.com/problems/merge-intervals/
#time: 79ms, beat 98%
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        if len(intervals) == 0:
            return []
        
        begin = intervals[0][0]
        end = intervals[0][1]
        
        ans = []
        
        for i in range (1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                ans.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
        ans.append([begin, end])
        return ans

#Link from leetcode: https://leetcode.com/problems/unique-number-of-occurrences/
#Summary: Check whether each character has different occurences
#example: arr = [1,2,2,1,1,3] --> True
#result: 32ms, beat 96.8%
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()
        
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        a = dict()
        
        for i in d:
            if d[i] not in a:
                a[d[i]] = 1
            else:
                return False
        return True

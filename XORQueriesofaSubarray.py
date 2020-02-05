#link:https://leetcode.com/contest/weekly-contest-170/problems/xor-queries-of-a-subarray/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        f = [0] * (len(arr) +1 )
        for i in range (1, len(arr) + 1):
            f[i] = f[i-1] ^ arr[i - 1]
        print(f)
        for i in queries:
            ans.append(f[i[1] + 1] ^ f[i[0]])
        return ans

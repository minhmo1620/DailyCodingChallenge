#This is the link from Leetcode: https://leetcode.com/problems/add-binary/
#Summary of the problem: Given 2 strings, each string contains '0' or '1'. In another word, they are binary string. 
#Question: How can we sum two of these strings 

#Example: 
    #Input: a = "11", b = "1"
    #Output: "100"

#My solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        x = int(a) + int(b)
        cnt = 0
        x = str(x)
        for i in range (len(x) - 1, -1,-1):
            if ( int(x[i]) + cnt ) == 2 :
                cnt = 1
                res += '0'
            elif ( int(x[i]) + cnt ) == 1:
                res += '1'
                cnt = 0
            elif ( int(x[i]) + cnt ) == 3:
                res += '1'
                cnt = 1
            else:
                res += '0'
                cnt = 0
        if cnt == 1:
            res += '1'
        return res[::-1]

#Performance of the solution: Beat 95.4% time
#yoyoyo
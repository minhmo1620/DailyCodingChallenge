#link problem: https://leetcode.com/problems/add-strings/
#Summary: Add two strings that you cannot use `int` to convert from string to integer from the first step
#result: 40ms, beat 87% time, 100% space

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1)) + num1
        elif len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        res = ''
        cnt = 0
        for i in range (len(num1) -1, -1, -1):
            if int(num1[i]) + int(num2[i]) + cnt >= 10:
                res = str((int(num1[i]) + int(num2[i]) + cnt)%10 ) + res
                cnt = 1
            else:
                res = str(int(num1[i]) + int(num2[i]) + cnt) + res
                cnt = 0
        if cnt == 1:
            return '1'+res
        return res

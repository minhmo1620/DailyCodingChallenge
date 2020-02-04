#link: https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = ""
        change = -1
        if len(palindrome) == 1:
            return ans
        for i in range (len(palindrome)//2):
            if palindrome[i] != "a":
                change = i
                break
        if change != -1:
            for i in range (len(palindrome)):
                if i == change:
                    ans += "a"
                else:
                    ans += palindrome[i]
        else:
            for i in range (len(palindrome)):
                if i == len(palindrome) - 1:
                    ans += "b"
                else:
                    ans += palindrome[i]
        return ans

# Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        d = []
        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            elif s[i] == ")":
                if len(st) > 0:
                    st.pop()
                else:
                    d.append(i)
            else:
                continue
        res = ""
        for i in range (len(s)):
            if i in st or i in d:
                continue
            else:
                res += s[i]
        return res
#link:
#time: 95%
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_s = {}
        hash_t = {}
        ans = None 
        for ch in s:
            if ch in hash_s:
                hash_s[ch] += 1
            else: 
                hash_s[ch] = 1 
        for char in t:
            if char not in hash_t:
                hash_t[char] = 1 
            else:
                hash_t[char] +=1 
        for char in t:
            if char not in hash_s:
                return char
            else:
                if hash_s[char] != hash_t[char]:
                    return char 
        # return char

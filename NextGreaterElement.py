#link: https://leetcode.com/problems/next-greater-element-i/
#48ms
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1)
        
        d = dict()
        for i in range (len(nums2)):
            d[nums2[i]] = -1
            for j in range (i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    d[nums2[i]] = nums2[j]
                    break
        res = []
        for i in nums1:
            res.append(d[i])
        return res

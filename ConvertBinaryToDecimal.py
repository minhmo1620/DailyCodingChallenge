#link:https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        
        cnt = 0
        lst = []
        while curr != None:
            if curr.val == 1:
                lst.append(True)
            else:
                lst.append(False)
            curr = curr.next
        ans = 0
        print(lst)
        for i in range (len(lst)):
            if lst[len(lst) - i - 1]:
                print(i)
                ans += 2**i
        return ans

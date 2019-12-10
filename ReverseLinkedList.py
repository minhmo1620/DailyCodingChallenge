#link: https://leetcode.com/problems/reverse-linked-list/submissions/
#Summary: Reverse a linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new = None
        
        curr = head
        
        while curr != None:
            tmp = curr.next
            curr.next = new
            new = curr
            curr = tmp
            
        return new
            

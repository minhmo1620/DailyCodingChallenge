#link: https://leetcode.com/problems/add-two-numbers-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseLinkedList(l):
            prev = None
            current = l
            head = prev
            while(current is not None): 
                next = current.next
                current.next = prev 
                prev = current 
                current = next
            return  prev
        def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
            cnt = 0
            p1 = l1
            p2 = l2
            p3 = ListNode(None)
            flag = False
            ans = p3
            
            while p1 != None or p2 != None:
                if flag:
                    p3.next = ListNode(None)
                    p3 = p3.next
                if p1 == None:
                    x = p2.val + cnt
                    p2 = p2.next
                elif p2 == None:
                    x = p1.val + cnt
                    p1 = p1.next
                else:
                    x = p1.val + p2.val + cnt
                    p1 = p1.next 
                    p2 = p2.next

                if x >= 10:
                    p3.val = (x % 10)
                    cnt = x // 10
                else:
                    p3.val = x
                    cnt = 0

                flag = True

            if cnt > 0:
                p3.next = ListNode(cnt)
            # print(p3)
            return ans  

        # print(addTwoNumbers(reverseLinkedList(l1), reverseLinkedList(l2)))
        return reverseLinkedList(addTwoNumbers(reverseLinkedList(l1), reverseLinkedList(l2)))
        
        

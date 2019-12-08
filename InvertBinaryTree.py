#link to Leetcode problem: https://leetcode.com/problems/invert-binary-tree/
#Summary: Flip the tree
#Result: 28ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = queue.Queue()
        
        q.put(root)
        
        while q.qsize() != 0:
            cur = q.get()
            if cur == None:
                continue
            if cur.left == None and cur.right == None:
                continue
            elif cur.left == None:
                cur.left = cur.right
                cur.right = None
                q.put(cur.left)
                
            elif cur.right == None:
                cur.right = cur.left
                cur.left = None
                q.put(cur.right)
            else:
                cur.left, cur.right = cur.right, cur.left
                q.put(cur.left)
                q.put(cur.right)
        return root
            
        

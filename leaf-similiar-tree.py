#link: https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leaf(self, root, lst):
        if root.left == None and root.right == None:
            lst.append(root.val)
            return 
        elif root.left == None:
            self.leaf(root.right, lst)
        elif root.right == None:
            self.leaf(root.left, lst)
        else:
            self.leaf(root.left, lst)
            self.leaf(root.right, lst)
        
            
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        lst1 = []
        lst2 = []
        self.leaf(root1, lst1)
        self.leaf(root2, lst2)
        return lst1==lst2

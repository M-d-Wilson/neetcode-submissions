import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        # NeetCode Answer
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        # My answer
        #temp1 = root.left
        #temp2 = root.right
        #root.right = self.invertTree(temp1)
        #root.left = self.invertTree(temp2)
        
        return root
            
        
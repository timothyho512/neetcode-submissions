# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # is balcned if height different is no more than 1

        # definitely dfs here

        # i think again same as last question

        # i definitely need a helper function here because I need the height from the left and right node from the root


        self.ans = True
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.ans = False
            return 1 + max(left, right)
        

        if not root:
            return True
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left - right) <= 1 and self.ans == True:
            return True
        
        return False
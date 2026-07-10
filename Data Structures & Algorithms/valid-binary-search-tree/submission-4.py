# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # so basically what we got here is for every node
        # we need to check if left side is smaller and rigth side is larger right
        def dfs(node, low, high):

            if not node:
                return True
            
            if node.val <= low:
                return False

            if node.val >= high:
                return False

            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            return left and right

        return dfs(root, float("-inf"), float("inf"))


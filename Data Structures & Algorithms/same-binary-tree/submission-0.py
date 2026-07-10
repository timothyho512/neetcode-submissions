# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # ok so a little be rusty here, havent done for 8 days

        # so i would need to slow down a bit and warm up a bit that is fine

        # so what we are looking at we need to have the exact same tree basically right

        # do i need a helper function, i think we need

        # i am thinking can i just go left and right with this isSameTree function

        # so something like:
        
        # forgot basecase here:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

            # and if both are true, so the subtree is fine, 
        if left and right:
            # we just need to look into the current node right?
            if p.val == q.val:
                return True

        return False
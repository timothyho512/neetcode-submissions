# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # so we need to bascailly go through the whole root and compare to the subRoot

        # so there are a few things

        #if the currrent node is the same, you go left and right together

        # if not you go left and right, while the subtree has to reset and point to thr root once again right

        # i am thinking if i need a helper functions here, 

        # i think this seems that i need a helper function no?

        # acutally i am not sure, no helper function because it returns bool which is what i need

        # yes helper function because i can save the answer in the global variables right (do i need it?)

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if p and not q:
                return False

            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

                # and if both are true, so the subtree is fine, 
            if left and right:
                # we just need to look into the current node right?
                if p.val == q.val:
                    return True

            return False

        # base case:
        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

   
        if left or right:
            return True
        return False
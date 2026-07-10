# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # so if i am not mistaken

        # lets summarise or reason or make things clear about what i need to do

        # so in this current tree,

        # if the value is either p or q (they are a single node, cant be a tree here)
        # then we need to check the root.left and root.right and see if they are p or q (to its case)
        # and if p or q is inside the root.left tree or root.right tree
        # then if yes, then the root is the thing we wanna return

        # so p or q co

        # if value is neitehr p or q
        # but root.left and root.right is p and q
        # or p and q is in root.left or root.right tree
        # then root is the thing we wanna return

        # so we need to scan through the whole root tree to find that 
        # node where p or q is not on the same side (if that is the case, there is the answer not here)
        # but either side (or one in the root)

        # so what is hard about this question


        # what i am thinking is we definitely want a helper function here
        # the reason for that is because i want to return true or false on if seeing p or q or not and not some random node right
        
        # and when we doing dfs here,
        # we are bascially doing bottom up which is exactly we want
        # i think we naturally find the lowest common ancester when it first came up
        # because we scan all left side first then right side, 

        # so naturally in this problem the first solution coming up is the one we want to return

        # so here, we can have a global vairable and self.var, and store some None, and if it is not empty, we immediately return that right
        

        # right now all the thinking is when there is no BST

        # and I completely missed that we are dealing with BST, and so we can use this to solve the problem

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # so what i think in this question is just get root.left and root.right and reverse it

        # and no, it is not that easy, because in every later, we need to reverse not just the top level

        # so we need to recurse here, i dont think it matters if we use dfs or bfs here
        # but dfs (meaning recursion) should be the easiest
        if not root:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left


        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # length is teh number of edge

        # and diameter here is the longest path or length between any tow nodes in the tree


        # so what is hard about this question

        # i think is the math here

        # base case
        
        # so for sure the function returns the diameter of the binary tree of that root

        # but lets say i get it here, one diameter on the left, one on the right, what can i use it for

        # I am thinking we need to use bfs instead of dfs here, 

        # because if we use dfs, the only info we can get form the child node is 
        # the diameter of that tree starting from that child node
        # but this info, the diameter, it doesnt mean anything, 

        # because what we want is, we need to find the maximum between few things
        # 1. 1+left_height +right_height
        # 2. max(answer from 1. , and left_return value, right return value)
        # but meaning we dont have the info of the height

        # but we only return one integer here, and it is the diameter

        # lets try to use bfs and solve this question


        # Nope, dont think it make sense to have bfs here.


        def getHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = getHeight(root.left)
            right = getHeight(root.right)

            return 1 + max(left, right)
        
        if not root:
            return 0
        
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)

        return max(left_height+right_height, left, right)




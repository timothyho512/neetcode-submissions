# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # this is a BST

        # i need to retrun a integer

        # so i need to find the kth smallest value

        # so what we can do here is to use the nature of the bst

        # the smallest value is always left left left .....

        # and the bottom left

        # the 2nd smallest is its parent

        # the 3rd is either the parent.right if there is

        # if not then parent again, and so on and on
        # so the rules is probably dfs

        # i am thinking if i need to have a helper function here or no, 

        # first to think is how do i know when it is the kth least,

        # so the order of work here is
        
        # go left
        # then do something, possibly add += 1 to the counter for the current node
        # then go right

        # then once the counter == k
        # and we return?
        # if that is the case, we would need a global counter and a helper function
        # or the helper function need to pass on the counter

        self.count = 0

        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            if left > -1:
                return left
            # do work 
            self.count += 1
            if self.count == k:
                return node.val

            right = dfs(node.right)
            if right > -1:
                return right

            return -1
        return dfs(root)
  


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # so between the node x itself and the root, there is no node that has a value greater than the node x including the root itself too

        # do definitely bfs right because we can logical go down node by node

        # but i am thinking dfs works fine here as well, e.g. if you go down left down the bottom
        # if you have a way to remember all node before, then that is fine too

        # i am not sure which one is easier tho

        # i am actually thinking dfs is easier becasue it is only saving the concerned node

        # while in bfs, because you are going to each height or level, you are saving some node that is not concerned to the current investigating node right

        # e.g. root = [2,1,1,3,null,1,5]
        # here if use bfs, then the second 1 is also saved which is not concerned to the left hand side
        # so that could become so messy right

        # lets say i have something that stored the concerned nodes, this could be a set or hashmap, or arrau
        # either of them are fine, just different implementation

        # but array should be the easiest becasue when you are removing, you are going to remove the latest one anyway

        # to be specific, so i need a stack here, not an array
        # and the stack is not storing the node or the value,
        # but it should be storing the current maximum right, so whne we pop, we know what is the next maximum you know
        if not root:
            return 0
        self.max_stack = []
        self.ans = 0
       
        def dfs(node):
            if not node:
                return
            if not self.max_stack:
                self.max_stack.append(node.val)
            else:
                self.max_stack.append(max(self.max_stack[-1], node.val))
            if self.max_stack[-1] <= node.val:
                self.ans += 1
            left = dfs(node.left)


            right = dfs(node.right)

            # remove back the thing
            self.max_stack.pop()
            return

        dfs(root)
        return self.ans

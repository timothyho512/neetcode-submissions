# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ok so here straight away i am thinking about the bfs again.

        # because that would be the most straight forward right, with the nature of bfs

        # and the hard part would be how do we know when we are at the mist right hand side of the node

        if not root:
            return []
        queue = deque()
        output = []
        queue.append(root)
        while queue:
            count = len(queue)
            for _ in range(len(queue)):
                
                node = queue.popleft()
                count -= 1

                if count == 0:
                    output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return output


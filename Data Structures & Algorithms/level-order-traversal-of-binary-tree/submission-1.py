# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # so here in this question what we need to return is something like:
        # Output: [[1],[2,3],[4,5,6,7]]

        # so basically what i am thinking straight away is something like a bfs instead

        # then have an array to store the output

        # then for the subarray, i am thinking we could just do counting and stop
        # because we know how many elements are there in a binary tree
        # always 1, 2, 4, 8, 16 something like that right
        if not root:
            return []

        queue = deque()

        output = []

        queue.append((root,0))
        current = []
        current_height = 0
        while queue:
            node, height = queue.popleft()

            if height > current_height:
                current_height = height
                output.append(current)
                current = []

            current.append(node.val)

            if node.left:
                queue.append((node.left, height + 1))
            if node.right:         
                queue.append((node.right, height + 1))

        if current:
            output.append(current)

        return output
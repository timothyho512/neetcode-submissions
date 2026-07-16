# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # values are unique, no duplicate
        # so what i need to return is a tree

        # and preorder is the array if the tree is walked with preorder

        # and inorder is the array if the tree is walked with inorder

        # one question that quicky came to my mind is that why do we need both to build the tree?
        # i believe we only need one of them no?

        # but now if i just look into the inorder array, i couldnt know if where is the root
        # like [2,1,3,4], it could be a lot of combination

        # while preorder, we definitely know the first item is the first element

        # now if we just have the preorder
        # we dont know when we finishing pushing to the left, millions of combination again
        # but because the inorder array, the first element of that is the bottom left, we know
        # we would know that when it finished going left and start to go right

        # so if we have an array (that is created by bfs) (level by level) we dont need all that
        # so a better way to think of is to build the array (that could have walked the bfs)

        # now i am struggling on the coding side, i am thinking what i could do right now
        # like what is a generic rule so that there is a way to the solution that can eb code,
        # this is where i am struggling to see right now
        # the repeatable procedure

        # hint by someone: once you know where the root is and 
        # where the left/right split is in the inorder array, 
        # what two smaller versions of "the same problem" are left over?

        # the answer to this question is [2,1,3,4]
        # so left side [2] and right side [3,4] would be the same two subproblem

        


        if not preorder:
            return None
        root = TreeNode(preorder[0])


        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                leftInorder = inorder[:i]
                rightInorder = inorder[i+1:]
                leftPreorder = preorder[1:len(leftInorder)+1]
                rightPreorder = preorder[len(leftInorder)+1:]
                break

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root
        

        

        
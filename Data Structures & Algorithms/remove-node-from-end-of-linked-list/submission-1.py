# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # so a few thoughts

        # again we could have just used the array

        # another i think would be go through the whole linked list once so we know the length
        # and then we could easily remove that specific node
        # but i think that is not the optimal solution they are looking for.

        # but that is the only thing I could think of

        right = head
        counter = 0
        while right:
            right = right.next
            counter += 1
        
        if counter == 1:
            return None
        # counter - n would be the index of the exact node we want to get rid of starting from 0 index
        index = counter - n
        if index == 0:
            return head.next
        curr = head
        while index - 1 > 0:
            curr = curr.next
            index -= 1
        
        curr.next = curr.next.next

        return head
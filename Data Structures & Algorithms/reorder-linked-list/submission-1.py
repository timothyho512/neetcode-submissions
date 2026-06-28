# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first i think can i turn this into a double linked list instead of singly so it is easier to work
        # second i think if i can turn this into an array but i think that is considered cheating

        # so the problem of this question is i think we need to have two pointer
        # one on the left pointing to the head
        # one on the tail pointing to the tail

        # then we can have a dummy head and then build the linked list there
        # and start moving the left pointer and the right pointer.

        # so the problem now is, how am i able to move the right pointer, because it does not have the information of the previous pointer.

        # so i am thinking there is two possibilities.
        # one is building the double linked list
        # another one is build a new list that is reversed.

        # right now I will try the second one first

        # Now when I finished this first draft, I get a problem.
        # with the condition while left != right
        # this only works when the list len is odd 
        # if it is even, this will never hit

        # so do i need to find somewhere to store the index number so we can compare in the while loop?

        if not head or not head.next:
            return
        # after hint we need to just reverse the second half
        slow = head
        slow_prev = None
        fast = head
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        # after this slow would be in the middle
        slow_prev.next = None


        reverse = slow
        prev = None

        while reverse:
            next_node = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = next_node

        left = head
        right = prev
        
        dummy = ListNode(0)
        tail = dummy

        while left and right:
            left_next = left.next
            right_next = right.next

            tail.next = left
            tail = tail.next

            tail.next = right
            tail = tail.next

            left = left_next
            right = right_next
        
        

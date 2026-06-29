# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # so i think the hardest part of this question is related to the math here,
        # so definitely there is some tricks that can easily do the math here

        # one question in my mind right now is why 0 is the edge case?

        # so from the math point of view, 
        # lets say normal number 209 + 902
        # where do we want to start here normally,
        # do we start from the left or from the right
        # i think from the right right? (so from the unit digit and then the tenth and hundreth)

        # because if we add 9 and 2, it gives 11, and we need to add 1 to the next unit

        # so starting from the right
        # and then add the digit together % 10 to get the result of the current unit
        # then sum digit together // 10 to to see if we really need to add 1 to the next unit or not

        # so if this is the case, we dont need to do anything to the linked list itself, no need to reverse, or anything because 
        # no reverse needed in either for doing math or the output

        # and we can have just a dummy for the output

        dummy = ListNode(0)

        tail = dummy

        left = l1
        right = l2
        next_u = 0

        while left and right:
            total = left.val + right.val + next_u

            this = total % 10

            next_u = total // 10

            # i am thinking if we should create a new node here or what

            tail.next = ListNode(this)

            tail = tail.next

            left = left.next
            right = right.next
        
        # now we could have one of the linked list left (one is bigger than the other)
        # or we could have the last unit (next_u) to be added

        while left:
            total = left.val + next_u
            this = total % 10
            next_u = total // 10
            tail.next = ListNode(this)
            tail = tail.next
            left = left.next
        while right:
            total = right.val + next_u
            this = total % 10
            next_u = total // 10
            tail.next = ListNode(this)
            tail = tail.next
            right = right.next
        
        if next_u:
            tail.next = ListNode(next_u)
        return dummy.next


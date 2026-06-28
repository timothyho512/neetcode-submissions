"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # syntax of creating new node: new_node = Node(val)

        # so here one thing to notice is, we just need the copy of the list
        # but no node in the original linked list should be pointed

        # this means we need to actually make a new node that has the same thing as the original node

        # what is so hard about the question
        # is ok we create the new node to copy the current node, but then the new_node.next and new_node.random is either empty for now
        # or pointing to the node in the orignal list
        # the .next is easy, because in the while loop, .next is created immediately and then we can just immediaetly do tail.next is the new made node

        # the problem is random, because it is random, if for example the firstnode.random is pointing to the last node, we need to wait unitl the last node because the new created node can point to that

        # so the problem is, how do we do that?

        # can we make a hashmap, and the key is node from the orignal node and the value is the new node tha copy that
        # and after finishing the while loop
        # we loop through the new list again to fill the random part?

        dummy = Node(0)
        tail = dummy

        hashmap = {}


        curr = head
        while curr:
            new_node = Node(curr.val)
            hashmap[curr] = new_node
            curr = curr.next
            
            tail.next = new_node
            tail = tail.next

        # for the last node, do i need to do this or is it fine?
        tail.next = None

        tail = dummy.next
        curr = head
        while tail and curr:
            tail.random = hashmap[curr.random] if curr.random else None
            tail = tail.next
            curr = curr.next

        return dummy.next


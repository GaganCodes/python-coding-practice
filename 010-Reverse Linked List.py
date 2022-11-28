# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case, if reached the end of the list
        if not head:
            return None
        
        # Recursive head
        new_head = head
        # Checking if recursion is possible
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return new_head


# Non-recursive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

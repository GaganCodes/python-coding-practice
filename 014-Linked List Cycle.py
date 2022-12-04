# Solution with O(1) memory complexity and O(n) time complexity

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
      
# Solution with O(n) memory complexity and O(n) time complexity
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        dict_node = dict()
        curr = head
        
        while curr:
            if curr in dict_node:
                return True
            dict_node[curr] = curr
            curr = curr.next
        return False


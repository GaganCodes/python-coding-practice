# First Attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check base case
        if root == p or root == q:
            return root
        
        if ((p.val < root.val) and (root.val < q.val)) or ((q.val < root.val) and (root.val < p.val)):
            # Check base case if p and q lie either side of root
            return root
        elif p.val > root.val and q.val > root.val:
            # If both p and q are on right side, recursive case
            ancestor = self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            # If both p and q are on left side, recursive case
            ancestor = self.lowestCommonAncestor(root.left, p, q)

        return ancestor
      
      
# More optimized/cleaner solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

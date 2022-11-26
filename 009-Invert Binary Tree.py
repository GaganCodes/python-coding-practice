# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Case for 1 node
        if root == None:
            # When we've reached the end
            return root
        elif root.left == None and root.right == None:
            # When we've no child
            return root
        elif root.left == None and root.right != None:
            # When we've only one child
            root.left = self.invertTree(root.right)
            root.right = None
        elif root.right == None and root.left != None:
            # When we've only one child
            root.right = self.invertTree(root.left)
            root.left = None
        else:
            # Recursive case
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)

        return root

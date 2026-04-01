# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None

        def inorder(node):
            if node is None:
                return True

            left_ok = inorder(node.left)
            if left_ok == False:
                return False

            if self.prev is not None and node.val <= self.prev:
                return False

            self.prev = node.val

            right_ok = inorder(node.right)
            if right_ok == False:
                return False

            return True

        return inorder(root)
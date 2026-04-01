# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # нашли узел

            # нет детей
            if root.left == None and root.right == None:
                return None

            # только правый
            if root.left == None:
                return root.right

            # только левый
            if root.right == None:
                return root.left

            # два ребенка
            cur = root.right
            while cur.left != None:
                cur = cur.left

            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)

        return root
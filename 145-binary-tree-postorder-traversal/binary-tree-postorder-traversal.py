# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = [] 

        def inorder(x):
            if x is None:
                return 
                
            inorder(x.left)
            inorder(x.right)
            result.append(x.val)
        
        inorder(root)
        return result     
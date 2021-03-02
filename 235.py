# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while (p.val - root.val) * (q.val - root.val) > 0:
            if p.val < root.val:
                root = root.left
            else:
                root = root.right
        return root

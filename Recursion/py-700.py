# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution for searching a binary search tree w/ recursion
    # TC: O(N) -> wrost case and O(logN) -> Best case
    # SC: O(1)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None or val == root.val:
            return root
        
        
        
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val) 
        
        
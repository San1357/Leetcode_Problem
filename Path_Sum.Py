''' Problem : Path Sum '''

#CODE :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
      if root is None:
        return False
      else:
        # Only leaf could return true
        if sum == root.val and root.left is None and root.right is None:
          return True
        else:
          return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

'''Problem :  Maximum_Depth_Of_Binary_Tree '''

#CODE :

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

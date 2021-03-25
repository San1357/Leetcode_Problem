'''Problem : Sum Row To Leaf Numbers '''

#CODE :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        return self.sumNumbersRecu(root, 0)
    
    def sumNumbersRecu(self, root, num):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return num * 10 + root.val
        
        return self.sumNumbersRecu(root.left, num * 10 + root.val) + self.sumNumbersRecu(root.right, num * 10 + root.val)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print (Solution().sumNumbers(root))    

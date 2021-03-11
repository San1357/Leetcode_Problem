'''Problem : Construct Binary Tree from Inorder and Postorder Traversal


#CODE : 

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = None
        
        def helper(root,inorder,postorder):
            
            root = TreeNode(postorder[-1])
            
            if len(inorder) is 1 and len(postorder) is 1:
                return root
            inorderHashmap = {}
            postorderHashmap = {}
            for i in range(len(inorder)):
                inorderHashmap[inorder[i]] = i
            for i in range(len(postorder)):
                postorderHashmap[postorder[i]] = i
            larr = inorder[:inorderHashmap[root.val]]
            rarr = inorder[inorderHashmap[root.val]+1:]
            if len(larr) and len(rarr):
                root.left = helper(root,larr,postorder[:0+len(larr)])
                root.right = helper(root,rarr,postorder[len(larr):-1])
            if len(larr) and len(rarr) is 0:
                root.left = helper(root,larr,postorder[:-1])
            if len(larr) is 0 and len(rarr):
                root.right = helper(root,rarr,postorder[:-1])
            return root
        return helper(root,inorder,postorder)

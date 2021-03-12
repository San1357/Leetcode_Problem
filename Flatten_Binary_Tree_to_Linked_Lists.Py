'''Problem : Flatten_Binary_Tree_To_Linked_Lists '''

#CODE :

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if root is None:
            return root

        # Stack for pre-order traverse
        S = [root]

        # Previous visited node
        prev_node = TreeNode(None)

        # Preorder traverse
        while S:
            N = S.pop()

            # Visit
            prev_node.left = None
            prev_node.right = N

            # Now N is the previously visited node
            prev_node = N

            # Push right which will be visited later
            if N.right:
                S.append(N.right)
            # Push left which will be visited earlier
            if N.left:
                S.append(N.left)

        # Set the last node
        prev_node.left = None
        prev_node.right = None

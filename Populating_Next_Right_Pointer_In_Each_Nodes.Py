'''Problem : Populating Next Right Pointers In Each Node '''

#CODE :

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        temp = root
        prev = root
        while temp != None:
            curr, prev = self.find_current(prev)
            if prev == None or curr == None:
                return root
            temp = curr
            while prev != None:
                if prev.left == curr:
                    if prev.right!=None:
                        curr.next = prev.right
                        curr = curr.next
                        prev = prev.next
                    else:
                        prev = prev.next
                elif prev.right == curr:
                    prev = prev.next
                else:
                    if prev.left != None:
                        curr.next = prev.left
                        curr=curr.next
                    elif prev.right!=None:
                        curr.next = prev.right
                        curr = curr.next
                        prev = prev.next
                    else:
                        prev = prev.next
            prev = temp
         
        return root
                             

    def find_current(self, node):
        while node!= None:
            if node.left!=None:
                return node.left, node
            elif node.right!=None:
                return node.right, node
            else:
                node = node.next
        return None, None

'''Problem : Populating Next Right Pointers In Each Node (II)


#CODE :

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        prev_child = None
        next_level = None
        
        while curr:
            child = curr.left if curr.left else curr.right
            
			# set starting point for next level traversal
            if next_level is None:
                next_level = child
              
			# connect current child to previous not Null child
            if prev_child:
                prev_child.next = child
            
			# connect left --> right of current node
            if curr.left and curr.right:
                curr.left.next = curr.right
                child = curr.right
            
			# only update prev_child when non-null child available
			# it's possible that this curr doesn't have children, but next curr has some
            if child:
                prev_child = child
            
			# continue level traversal
            curr = curr.next
            
			# finished current level, traverse next level
			# if next level is None then we are done
            if curr is None:
                curr = next_level
                next_level = None
                prev_child = None
        
        return root

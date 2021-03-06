'''Problem : remove_dublicates_from_sorted_Array '''

#CODE : 

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        # Handle special case that the list is empty
        if head == None:        return head
        current = head
        # Travel the list until the second last node
        while current.next != None:
            if current.val == current.next.val:
                # This element and the next one are the same.
                # They are duplicate. We are going to remove
                # the next node.
                temp = current.next
                current.next = current.next.next
                del temp
            else:
                current = current.next
        return head

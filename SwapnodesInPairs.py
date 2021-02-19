'''
Problem : Swap Nodes in pairs


#CODE :


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        curr = head

        while(curr!=None and curr.next!=None):
            curr_val = curr.val
            nextNode = curr.next
            curr.val = nextNode.val
            nextNode.val = curr_val
            curr = curr.next.next
        return head

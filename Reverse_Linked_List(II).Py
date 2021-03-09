'''Problem : Reverse Linked List (II)

#CODE :


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:          return head
        
        currentNode = pseoduHead = ListNode(-1)
        pseoduHead.next = head
        current = 0
        
        while current < m - 1:
            currentNode = currentNode.next
            current += 1
        beforeReverseZone = currentNode
        
        stack = []
        for _ in range(m, n+1):
            stack.append(currentNode.next)
            currentNode = currentNode.next
        
        afterReverseZone = currentNode.next
        
        
        reverseListEnd = reverseListHead = stack.pop()
        while len(stack) != 0:
            reverseListEnd.next = stack.pop()
            reverseListEnd = reverseListEnd.next
        
        beforeReverseZone.next = reverseListHead
        reverseListEnd.next = afterReverseZone
        
        return pseoduHead.next

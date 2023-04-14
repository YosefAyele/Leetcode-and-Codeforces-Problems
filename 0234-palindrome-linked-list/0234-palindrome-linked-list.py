class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        def reverse(head):
            previous = None
            current = head
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous

        def secondhalf(head):
            fast = head
            slow = head
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        # Find the end of first half and reverse second half.
        
        second = reverse(secondhalf(head).next)

        # Check
        res = True
        pointer1 = head
        pointer2 = second
        while res and pointer2 is not None:
            if pointer1.val != pointer2.val:
                res = False
            pointer1 = pointer1.next
            pointer2 = pointer2.next

    
        
        return res   


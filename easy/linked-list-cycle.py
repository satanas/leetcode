# Use two pointers (fast and slow)
# We iterate until fast reaches the end of the list (no cycle)
# Or until they meet (cycle)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        # Single node list
        if head is None or head.next is None:
            return False
        
        fast = head.next
        slow = head
        
        while True:
            if fast is not None and slow is not None and fast.val == slow.val:
                return True

            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next

            

if __name__ == "__main__":
    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node4 = ListNode(-4)
    
    node3.next = node2
    node2.next = node0
    node0.next = node4
    node4.next = node2
    s = Solution()
    print(s.hasCycle(node3))

    node3.next = None
    print(s.hasCycle(node3))
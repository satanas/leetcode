class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        first = None
        prev = None
        curr1 = l1
        curr2 = l2
        carry_over = 0

        while curr1 or curr2:
            v1 = 0 if curr1 is None else curr1.val
            v2 = 0 if curr2 is None else curr2.val

            new_value = v1 + v2 + carry_over
            carry_over = 0
            if new_value > 9:
                new_value = new_value % 10
                carry_over = 1
            
            curr_sum = ListNode(new_value)
            
            if first is None:
                first = curr_sum
            if prev is not None:
                prev.next = curr_sum

            prev = curr_sum
            curr1 = curr1.next if curr1 is not None else None
            curr2 = curr2.next if curr2 is not None else None

        if carry_over > 0:
            curr_sum = ListNode(carry_over)
            prev.next = curr_sum

        return first

if __name__ == "__main__":
    s = Solution()
    # l1 = ListNode(2, ListNode(4, ListNode(3)))
    # l2 = ListNode(5, ListNode(6, ListNode(4)))
    l1 = ListNode(2)
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next

# Definition for singly-linked list.
# Input: 1->2->3->4->5->NULL
#    *
# 1->3->4->5->NULL
# f   *
# 2->4->5->NULL

#       * (odd)
# 1->3->5->NULL
# f  x
# 2->4->NULL

# last odd point to first even

# 1->3->5->2->4->NULL

# Output: 1->3->5->2->4->NULL

# Input: 1->2->3->4->NULL
# Output: 1->3->2->4->NULL

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, root):
        if root.next is None or root is None:
            return root

        curr_odd = root
        last_odd = root
        curr_even = root.next
        first_even = root.next

        while curr_odd is not None or curr_even is not None:
            if curr_odd:
                print(f"curr odd: {curr_odd.val}")
            if curr_even:
                print(f"curr even: {curr_even.val}")
            
            last_odd = curr_odd
            next_odd = None
            if curr_odd is not None and curr_odd.next is not None and curr_odd.next.next is not None:
                next_odd = curr_odd.next.next
                print(f"next odd: {next_odd.val}")
                curr_odd.next = next_odd
            curr_odd = next_odd

            next_even = None
            if curr_even is not None and curr_even.next is not None and curr_even.next.next is not None:
                next_even = curr_even.next.next
                print(f"next even: {next_even.val}")
                curr_even.next = next_even
            curr_even = next_even
            print("-----")
            
        print(f"curr odd: {last_odd.val}")
        last_odd.next = first_even
        return root

def print_nodes(root):
    text = ""
    curr = root
    print(root.next)
    while curr.next is not None:
        text += f"{curr.val}->"
        print(curr.next)
        curr = curr.next
    print(text)

if __name__ == "__main__":
    s = Solution()
    print_nodes(s.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
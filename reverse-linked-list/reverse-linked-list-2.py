# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Whilst we traverse the list we change the curr.next to point to the previous element
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == "__main__":
    five = ListNode(5)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)

    curr = one
    while curr is not None:
        print(curr.val)
        curr = curr.next

    s = Solution()
    curr = s.reverseList(one)

    print("---")

    while curr is not None:
        print(curr.val)
        curr = curr.next
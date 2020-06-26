# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
            
        stack = []
        self.traverse(head, stack)

        root = ListNode(stack.pop())
        curr = root
        while len(stack) > 0:
            val = stack.pop()
            if val is not None:
                curr.next = ListNode(val)
                curr = curr.next

        return root

    def traverse(self, node, stack):
        stack.append(node.val)
        if node.next is None:
            return
        else:
            self.traverse(node.next, stack)


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
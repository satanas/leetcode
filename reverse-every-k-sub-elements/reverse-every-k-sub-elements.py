from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_every_k_elements(head, k):
    previous = None
    seg_start = None
    before_seg = None
    curr = head
    i = 1
    while curr.next is not None:
        if i % k == 1:
            seg_start = curr
        if i % k == 0:
            if before_seg is None:
                head = curr
            else:
                before_seg.next = curr
            
            before_seg = seg_start

        next = curr.next
        curr.next = previous
        previous = curr
        curr = next
        i += 1
    
    before_seg.next = curr
    curr.next = previous
    previous.next = None
    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

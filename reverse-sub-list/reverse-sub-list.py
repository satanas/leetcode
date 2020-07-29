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

def reverse_sub_list(head, p, q):
    curr = head
    node_before_sub_list = head
    i = 0
    # Skip p-1 nodes
    while curr is not None and i < p - 1:
        node_before_sub_list = curr
        curr = curr.next
        i += 1

    # reverse sub-list
    p_node = node_before_sub_list.next
    previous = None
    while curr is not None and curr.value <= q:
        next = curr.next
        curr.next = previous
        previous = curr
        if curr.value == q:
            q_node = curr
        curr = next

    node_before_sub_list.next = q_node
    p_node.next = curr

    return head
       

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    #result = reverse_sub_list(head, 2, 4)
    #print("Nodes of reversed LinkedList are: ", end='')
    #result.print_list()
    result = reverse_sub_list(head, 0, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
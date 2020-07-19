class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_cycle_start(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_length = calculate_cycle_length(slow)
            break

    pointer1, pointer2 = head, head
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer2

def calculate_cycle_length(slow):
    current = slow
    length = 1
    current = current.next
    while current != slow:
        current = current.next
        length += 1
    return length


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


if __name__ == "__main__":
    main()
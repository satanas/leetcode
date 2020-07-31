from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            elem = queue.popleft()
            level_sum += elem.val

            if elem.left is not None:
                queue.append(elem.left)
            if elem.right is not None:
                queue.append(elem.right)
            
        level_avg = level_sum / level_size
        result.append(level_avg)
    return result

if __name__ == "__main__":
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))
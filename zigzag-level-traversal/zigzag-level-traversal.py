from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    ltr = True
    queue.append(root)
    while len(queue) > 0:
        level_size = len(queue)
        level = []
        for i in range(level_size):
            x = queue.popleft()
            if x.left is not None:
                queue.append(x.left)
            if x.right is not None:
                queue.append(x.right)
            if ltr:
                level.append(x.val)
            else:
                level.insert(0, x.val)

        result.append(level)
        ltr = not ltr

    return result

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))
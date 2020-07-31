class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    all_paths = []
    recursive_find(root, sum, 0, all_paths)
    return len(all_paths)

def recursive_find(node, total_sum, curr_sum, all_paths):
    if node.val + curr_sum == total_sum and node.left is None and node.right is None:
        all_paths.append(1)
    else:
        if node.left is not None:
            recursive_find(node.left, total_sum, curr_sum + node.val, all_paths)
        if node.right is not None:
            recursive_find(node.right, total_sum, curr_sum + node.val, all_paths)

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
                ": " + str(find_paths(root, sum)))
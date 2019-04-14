"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
  /\
 7 9
Return [[1, 2], [1, 3, 4,7], [1, 3, 4,9], [1, 3, 5]].
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def collect_paths(paths, root):
    if (root == None):
        return

    paths.append(root.data)

    if (root.left == None and root.right == None):
        print(paths)
        paths.pop()
        # return paths

    collect_paths(paths, root.left)
    paths.pop()
    collect_paths(paths, root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.left = Node(7)
root.right.left.right = Node(9)
root.right.right = Node(5)


collect_paths([], root)

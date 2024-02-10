from typing import List


class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    @staticmethod
    def createTree(input: List[int]) -> Node:
        if not input:
            return None

        root = Node(input[0])
        stack = [(root, 0)]
        index = 2  # Start from the second element

        while stack and index < len(input):
            parent, depth = stack.pop(0)
            while index < len(input) and input[index] is not None:
                child = Node(input[index])
                parent.children.append(child)
                stack.append((child, depth + 1))
                index += 1
            index += 1

        return root

    @staticmethod
    def traverseTree(root: Node) -> List[int]:
        if root is None:
            return []

        result = []
        for child in root.children:
            result.extend(Solution.traverseTree(child))

        result.append(root.val)
        return result


# Test the implementation
if __name__ == "__main__":
    input_example = [1, None, 3, 2, 4, None, 5, 6]
    root = Solution.createTree(input_example)
    postorder_traversal = Solution.traverseTree(root)
    print(postorder_traversal)

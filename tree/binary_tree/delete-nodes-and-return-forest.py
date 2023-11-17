from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)

        if not root:
            return result

        if root.val not in to_delete:
            result.append(root)

        # Using a BFS approach with a deque for efficient O(1) popleft
        queue = deque([(root, None)])  # (current node, parent node)

        while queue:
            node, parent = queue.popleft()

            # If the node is to be deleted
            if node.val in to_delete:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None

                # Add children of deleted node as new trees
                if node.left:
                    if node.left.val not in to_delete:
                        result.append(node.left)
                    queue.append((node.left, None))

                if node.right:
                    if node.right.val not in to_delete:
                        result.append(node.right)
                    queue.append((node.right, None))

            else:
                # Continue BFS
                if node.left:
                    queue.append((node.left, node))

                if node.right:
                    queue.append((node.right, node))

        return result

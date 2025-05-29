from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self, arr):
        self.problem = arr
        self.root = self.build_binary_tree()  # Store the tree once during initialization

    def height(self, root):
        if root is None:
            return -1  # height in terms of edges
        l = self.height(root.left)
        r = self.height(root.right)
        return max(l, r) + 1

    def build_binary_tree(self):
        if not self.problem or self.problem[0] is None:
            return None
        root = Node(self.problem[0])
        queue = deque([root])
        i = 1
        while queue and i < len(self.problem):
            current = queue.popleft()
            # Left child
            if i < len(self.problem) and self.problem[i] is not None:
                current.left = Node(self.problem[i])
                queue.append(current.left)
            i += 1
            # Right child
            if i < len(self.problem) and self.problem[i] is not None:
                current.right = Node(self.problem[i])
                queue.append(current.right)
            i += 1
        return root

    def solve(self):
        return self.height(self.root)

    # In-order DFS: Left, Root, Right
    def in_order_dfs(self, node):
        if node is None:
            return
        self.in_order_dfs(node.left)
        print(node.data, end=' ')
        self.in_order_dfs(node.right)

    # Pre-order DFS: Root, Left, Right
    def pre_order_dfs(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.pre_order_dfs(node.left)
        self.pre_order_dfs(node.right)

    # Post-order DFS: Left, Right, Root
    def post_order_dfs(self, node):
        if node is None:
            return
        self.post_order_dfs(node.left)
        self.post_order_dfs(node.right)
        print(node.data, end=' ')

    # BFS: Level order traversal
    def bfs(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Use the class
arr = [12, 8, 18, 5, 12]
solution = Solution(arr)

print("Height of tree:", solution.solve())

print("\nIn-order DFS:")
solution.in_order_dfs(solution.root)

print("\nPre-order DFS:")
solution.pre_order_dfs(solution.root)

print("\nPost-order DFS:")
solution.post_order_dfs(solution.root)

print("\nBFS (Level Order):")
solution.bfs()

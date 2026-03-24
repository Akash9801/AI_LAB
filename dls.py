class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def depth_limited_search(node, limit, visited):
    if node is None:
        return

    # Visit the current node
    visited.append(node.value)

    # If depth limit reached, stop expanding
    if limit == 0:
        return

    # Recur for children
    for child in node.children:
        depth_limited_search(child, limit - 1, visited)


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

root.children = [node2, node3]
node2.children = [node4, node5]
node3.children = [node6, node7]

# --------- Run DLS ---------
limit = 2
visited_nodes = []
depth_limited_search(root, limit, visited_nodes)

print(f"DLS (limit={limit}): Visited nodes {visited_nodes}")
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def depth_limited_search(node, limit, visited):
    if node is None:
        return

    visited.append(node.value)

    if limit == 0:
        return

    for child in node.children:
        depth_limited_search(child, limit - 1, visited)


def iddfs(root, max_depth):
    for depth in range(max_depth + 1):
        visited_nodes = []
        depth_limited_search(root, depth, visited_nodes)
        print(f"Depth Limit {depth}: Visited nodes {visited_nodes}")



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

# --------- Run IDDFS ---------
iddfs(root, 2)
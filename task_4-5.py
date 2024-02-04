import numpy as np
import heapq
import matplotlib.pyplot as plt
import networkx as nx
import uuid


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


class BinaryHeap:
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            self.build_heap(values)

    def build_heap(self, values):
        for value in values:
            self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if not current.left:
                    current.left = Node(value)
                    break
                else:
                    queue.append(current.left)
                if not current.right:
                    current.right = Node(value)
                    break
                else:
                    queue.append(current.right)

    def dfs(self, node, visit_func):
        if node:
            visit_func(node)
            self.dfs(node.left, visit_func)
            self.dfs(node.right, visit_func)

    def bfs(self, visit_func):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current:
                visit_func(current)
                queue.append(current.left)
                queue.append(current.right)


class BinaryHeapVisualizer:
    @staticmethod
    def visualize_traversal(node, traversal_func):
        color_map = []
        counter = [0]
        graph = nx.DiGraph()
        pos = {}

        def visit_func(node):
            color = "#{:02x}{:02x}ff".format(
                min(255, 30 + counter[0] * 10), min(255, 100 + counter[0] * 10)
            )
            node.color = color
            color_map.append((node.id, node.color))
            counter[0] += 1

        if traversal_func == "dfs":
            BinaryHeap().dfs(node, visit_func)
        else:  # BFS
            BinaryHeap().bfs(visit_func)

        BinaryHeapVisualizer._build_graph(node, graph, pos)
        colors = [data["color"] for node_id, data in graph.nodes(data=True)]

        labels = {node: data["label"] for node, data in graph.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(
            graph,
            pos=pos,
            node_color=colors,
            labels=labels,
            with_labels=True,
            arrows=False,
            node_size=2500,
        )
        plt.show()

    @staticmethod
    def _build_graph(node, graph=None, pos={}, x=0, y=0, layer=0):
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)
            pos[node.id] = (x, y)
            layer_gap = 1 / (2 ** (layer + 1))
            if node.left:
                graph.add_edge(node.id, node.left.id)
                BinaryHeapVisualizer._build_graph(
                    node.left, graph, pos, x=x - layer_gap, y=y - 1, layer=layer + 1
                )
            if node.right:
                graph.add_edge(node.id, node.right.id)
                BinaryHeapVisualizer._build_graph(
                    node.right, graph, pos, x=x + layer_gap, y=y - 1, layer=layer + 1
                )
        return graph, pos


def main():
    values = [1, 3, 2, 7, 6, 4, 5]
    heap = BinaryHeap(values)
    print("DFS Traversal Visualization:")
    BinaryHeapVisualizer.visualize_traversal(heap.root, "dfs")
    print("BFS Traversal Visualization:")
    BinaryHeapVisualizer.visualize_traversal(heap.root, "bfs")


if __name__ == "__main__":
    main()

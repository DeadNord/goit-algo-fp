import numpy as np
import heapq
import matplotlib.pyplot as plt
import networkx as nx


class Dijkstra:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = np.array(adjacency_matrix)
        self.vertices = self.adjacency_matrix.shape[0]

    def find_shortest_path(self, start_vertex):
        distances = np.inf * np.ones(self.vertices)
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in range(self.vertices):
                if self.adjacency_matrix[current_vertex, neighbor] != np.inf:
                    distance = (
                        current_distance
                        + self.adjacency_matrix[current_vertex, neighbor]
                    )
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))

        return distances


class GraphVisualizer:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = np.array(adjacency_matrix)

    def visualize(self):
        G = nx.DiGraph()
        rows, cols = self.adjacency_matrix.shape

        for i in range(rows):
            for j in range(cols):
                if (
                    self.adjacency_matrix[i, j] != np.inf
                    and self.adjacency_matrix[i, j] > 0
                ):
                    G.add_edge(i, j, weight=self.adjacency_matrix[i, j])

        pos = nx.spring_layout(G)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=700,
            node_color="skyblue",
            edge_color="k",
            width=1,
            linewidths=1,
            font_size=15,
            arrows=True,
            arrowsize=20,
        )

        edge_labels = dict(
            [
                (
                    (
                        u,
                        v,
                    ),
                    d["weight"],
                )
                for u, v, d in G.edges(data=True)
            ]
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()


if __name__ == "__main__":
    adjacency_matrix = [
        [0, 4, 1, np.inf, np.inf],
        [np.inf, 0, np.inf, np.inf, 4],
        [np.inf, 2, 0, 4, np.inf],
        [np.inf, np.inf, np.inf, 0, 4],
        [np.inf, np.inf, np.inf, np.inf, 0],
    ]

    dijkstra_solver = Dijkstra(adjacency_matrix)
    start_vertex = 0
    distances = dijkstra_solver.find_shortest_path(start_vertex)
    print(f"Shortest paths from vertex {start_vertex} to others:", distances)

    visualizer = GraphVisualizer(adjacency_matrix)
    visualizer.visualize()

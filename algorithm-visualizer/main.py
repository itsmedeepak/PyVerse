from collections import deque
import heapq
from graph_examples import example_graph, weighted_graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend([n for n in graph.get(node, []) if n not in visited])
    return order

def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            stack.extend([n for n in reversed(graph.get(node, [])) if n not in visited])
    return order

def ucs(graph, start):
    visited = set()
    queue = [(0, start)]
    order = []

    while queue:
        cost, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            order.append((node, cost))
            neighbors = graph.get(node, {})
            # handle both dict (weighted) and list (unweighted)
            if isinstance(neighbors, dict):
                for neighbor, weight in neighbors.items():
                    if neighbor not in visited:
                        heapq.heappush(queue, (cost + weight, neighbor))
            else:  # assume unweighted -> weight = 1
                for neighbor in neighbors:
                    if neighbor not in visited:
                        heapq.heappush(queue, (cost + 1, neighbor))
    return order

def visualize():
    print("Graph Nodes:", list(example_graph.keys()))
    start = input("Enter start node: ")

    print("\nBFS Order:", bfs(example_graph, start))
    print("DFS Order:", dfs(example_graph, start))
    print("UCS Order (node, cumulative cost):", ucs(weighted_graph, start))

if __name__ == "__main__":
    visualize()

import heapq

def dijkstra(graph, start):
    """
    Find the shortest path from start node to all other nodes using Dijkstra's algorithm.
    
    Args:
        graph (dict): adjacency list {node: [(neighbor, weight), ...]}
        start (any): starting node
    
    Returns:
        dict: shortest distance to each node from start
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]  # (distance, node)

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
        'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
        'E': [('C', 8), ('D', 3)],
        'F': [('D]()

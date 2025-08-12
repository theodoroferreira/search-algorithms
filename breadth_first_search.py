from collections import deque


def bfs(graph, start_node):
    if start_node not in graph:
        return

    queue = deque([start_node])
    visited_nodes = {start_node}
    result = []

    while queue:

        current_node = queue.popleft()
        result.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                queue.append(neighbor)

    return result

def dfs(graph, start_node):
    if start_node not in graph:
        return

    stack = [start_node]
    visited_nodes = list()

    while stack:
        current_node = stack.pop()

        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            for neighbor in reversed(list(graph[current_node])):
                if neighbor not in visited_nodes:
                    stack.append(neighbor)

    return visited_nodes

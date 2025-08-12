import breadth_first_search
import depth_first_search


def main():
    graph = {
        0: {1, 2},
        1: {3, 4},
        2: {5, 6},
        3: set(),
        4: set(),
        5: set(),
        6: set(),
    }
    result_breadth = breadth_first_search.bfs(graph, 0)
    print(result_breadth)
    result_depth = depth_first_search.dfs(graph, 0)
    print(result_depth)


if __name__ == '__main__':
    main()

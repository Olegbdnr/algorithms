row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, -1, 1, -2, 2, -2, 2]


def get_neighbours(vertex):
    neighbours = []
    for i in range(8):
        if 0 <= vertex[0] + row[i] <= 7:
            if 0 <= vertex[1] + col[i] <= 7:
                neighbours.append((vertex[0] + row[i], vertex[1] + col[i]))

    return neighbours


def in_list(vertex, list):
    for item in list:
        if item == vertex:
            return True


def get_shortest_path(start, end, path):
    result = []
    result.insert(0, path[end])
    while result[0] != start:
        result.insert(0, path[result[0]])
    return len(result)


def bfs(start, end):
    queue = []
    visited = []
    queue.append(start)
    path = {}

    while queue:
        current = queue.pop(0)
        if current == end:
            return get_shortest_path(start, end, path)
        visited.append(current)
        neighbours = get_neighbours(current)
        for neighbour in neighbours:
            if not in_list(neighbour, queue) and not in_list(neighbour, visited):
                queue.append(neighbour)
                path[neighbour] = current


def main():
    start = (0, 7)
    end = (7, 0)
    path = bfs(start, end)
    print(path)


if __name__ == main():
    main()

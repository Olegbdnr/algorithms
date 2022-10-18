def is_boy(number):
    if number % 2 > 0:
        return True
    else:
        return False


def get_neighbours(vertex, tribes):
    neighbours = []
    for i in range(len(tribes)):
        if tribes[i][0] == vertex:
            neighbours.append(tribes[i][1])
    return neighbours


def get_first_tribe(tribes):
    stack = []
    visited = []
    stack.insert(0, tribes[0][0])
    while stack:
        current = stack.pop(0)
        visited.append(current)
        neighbours = get_neighbours(current, tribes)
        if neighbours not in visited and neighbours not in stack:
            for n in neighbours:
                stack.insert(0, n)
    return visited


def get_second_tribe(first_tribe, tribes):
    second_tribe = []
    for i in range(len(tribes)):
        if tribes[i][0] not in first_tribe:
            if tribes[i][0] not in second_tribe:
                second_tribe.append(tribes[i][0])
            if tribes[i][1] not in second_tribe:
                second_tribe.append(tribes[i][1])
    return second_tribe


def get_wedding_combinations(first, second):
    res = 0
    for i in range(len(first)):
        for j in range(len(second)):
            if is_boy(first[i]) and not is_boy(second[j]) or not is_boy(first[i]) and is_boy(second[j]):
                res += 1
    return res


def main():
    graph = [(1, 2),
             (2, 4),
             (1, 3),
             (3, 5),
             (8, 10)
             ]
    first_tribe = get_first_tribe(graph)
    second_tribe = get_second_tribe(first_tribe, graph)
    print(first_tribe)
    print(second_tribe)
    print(get_wedding_combinations(first_tribe, second_tribe))


if __name__ == "__main__":
    main()

from math import sqrt


def get_wire_length(pillars, length):
    if len(pillars) == 1:
        return 0
    first = pillars[0]
    pillars.pop(0)
    return sqrt(((first - pillars[0]) * (-1)) *
                ((first - pillars[0]) * (-1)) +
                length * length) + get_wire_length(pillars, length)


print(get_wire_length([3, 1, 3], 2))

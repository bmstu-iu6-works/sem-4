import itertools


def get_map(graph):
    result = {}

    for src, dest in graph.keys():
        if src in result:
            result[src].append(dest)
        else:
            result[src] = [dest]

    return result


def get_rev_map(graph):
    result = {}

    for src, dest in graph.keys():
        if dest in result:
            result[dest].append(src)
        else:
            result[dest] = [src]

    return result


def find_start(graph):
    return min(itertools.chain(*graph.keys()))


def find_end(graph):
    return max(itertools.chain(*graph.keys()))


def lagged_path(path):
    return [(path[i], path[i + 1]) for i in range(len(path) - 1)]

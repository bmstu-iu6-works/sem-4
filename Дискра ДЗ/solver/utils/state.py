from .path import lagged_path


def state_from_apply(graph, state: dict, path, delta):
    result = state.copy()

    for pair in lagged_path(path):
        rev_pair = tuple(reversed(pair))
        if pair in graph:
            cur = result.get(pair, 0)
            mx = graph[pair]
            assert cur + delta <= mx, f'{pair} is not in delta({delta + cur} >= {mx})'

            result[pair] = cur + delta
        elif rev_pair in graph:
            cur = result.get(rev_pair, 0)
            assert cur >= delta, f'{pair} is not in delta({cur} - {delta})'

            result[rev_pair] = cur - delta
        else:
            raise ValueError(f'{pair} is not in graph')

    return result


def get_positive_flow_part(graph, state, path):
    result = []

    for pair in lagged_path(path):
        if pair in graph:
            result.append(graph[pair] - state.get(pair, 0))

    return result


def get_negative_flow_part(graph, state, path):
    result = []

    for pair in lagged_path(path):
        rev_pair = tuple(reversed(pair))
        if rev_pair in graph:
            result.append(state.get(rev_pair, 0))

    return result


def state_to_set(state):
    return set((k[0], k[1], v) for k, v in state.items())


def get_fulfilled_parts(graph, old_state, new_state):
    old_set = state_to_set(old_state)
    new_set = state_to_set(new_state)

    diff = new_set - old_set

    result = []
    for src, dest, val in diff:
        pair = src, dest
        mx = graph[pair] if pair in graph else graph[tuple(reversed(pair))]
        if mx == val:
            result.append(pair)
    return result

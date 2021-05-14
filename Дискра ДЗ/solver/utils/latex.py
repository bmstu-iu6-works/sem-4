from .path import lagged_path
from .state import get_fulfilled_parts


def repr_path(path):
    parts = ["x_{%s}" % str(part) for part in path]
    return "(" + ", ".join(parts) + ")"


def repr_delta(graph, state, path):
    parts = []

    for pair in lagged_path(path):
        if pair in graph:
            parts.append(f"{graph[pair]}-{state.get(pair, 0)}")

    # ,<short space>
    mx = r",\,".join(parts)
    return r"\delta^*=min\{" + mx + r"\}"


def repr_xi(state, path):
    parts = []

    for pair in lagged_path(path):
        rev_pair = tuple(reversed(pair))
        if rev_pair in state:
            parts.append(f"{str(state.get(rev_pair))}")

    # ,<short space>
    mx = r",\,".join(parts)
    return r"\xi^*=min\{" + mx + r"\}"


def draw_formulas(graph, result_flow, path, state, delta, xi=0):
    result = "\n"
    result += r"\being{gather*}" + "\n"
    result += (repr_delta(graph, state, path) + f"={delta}") + "\\\\\n"
    if xi:
        result += (repr_xi(state, path) + f"={xi}") + "\\\\\n"
        delta = min(delta, xi)
    result += (r"\varphi = " + str(result_flow) + "+" + str(delta) + "=" + str(result_flow + delta)) + "\n"
    result += r"\end{gather*}" + "\n"
    return result


def draw_fulfilled(graph, old_state, new_state):
    result = "\n"

    fulfilled = get_fulfilled_parts(graph, old_state, new_state)
    if not fulfilled:
        return result

    result += "Насыщенны:\n"
    result += r"\begin{itemize}" + "\n"
    for fulfilled in map(repr_path, fulfilled):
        result += (r"\item " + fulfilled) + "\n"
    result += r"\end{itemize}" + "\n"

    return result

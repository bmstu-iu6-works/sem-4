from utils.dot import draw_digraph
from utils.path import find_start, find_end, get_map, get_rev_map
from utils.state import get_positive_flow_part, get_negative_flow_part, state_from_apply
from utils.latex import repr_path, draw_formulas, draw_fulfilled


def find_accessable(graph, state):
    path = [find_start(graph)]
    final = find_end(graph)
    pos_map = get_map(graph)
    rev_map = get_rev_map(graph)

    to_visit = {find_start(graph)}
    visited = set()
    result = set()

    while to_visit - visited:
        for first in list(to_visit - visited):
            maps = [*(pos_map[first]), *rev_map.get(first, [])]
            visited |= {first}
            for second in maps:

                pair = (first, second)
                is_reverse = pair not in graph

                cur = state.get(tuple(reversed(pair)), 0) if is_reverse else state.get(pair, 0)

                exceed_flow = cur == 0 if is_reverse else cur == graph[pair]
                if exceed_flow or second == final:
                    continue
                result |= {first}
                to_visit |= {second}

    return list(result)


def find_path(graph, state, path=None, final=None, pos_map=None, rev_map=None, allow_reverse=False):
    if path is None:
        path = [find_start(graph)]

    if final is None:
        final = find_end(graph)

    if pos_map is None:
        pos_map = get_map(graph)

    if rev_map is None:
        rev_map = get_rev_map(graph)

    first = path[-1]

    result = []
    maps = [*(pos_map[first]), *rev_map.get(first, [])]
    for second in maps:
        pair = (first, second)
        is_reverse = pair not in graph

        if is_reverse and not allow_reverse:
            return

        cur = state.get(tuple(reversed(pair)), 0) if is_reverse else state.get(pair, 0)

        exceed_flow = cur == 0 if is_reverse else cur == graph[pair]
        if second in path or exceed_flow:
            continue

        if second == final:
            return [*path, final]

        new_result = find_path(graph, state, [*path, second], final, pos_map, rev_map, allow_reverse=allow_reverse,
                               )
        if new_result:
            return new_result


def main():
    graph = {
        (1, 2): 9,
        (1, 3): 3,
        (1, 4): 20,
        (1, 5): 41,

        (2, 3): 5,
        (2, 12): 10,

        (3, 4): 29,
        (3, 6): 5,
        (3, 7): 2,

        (4, 6): 14,
        (4, 8): 22,

        (5, 4): 27,
        (5, 8): 15,
        (5, 10): 18,

        (6, 2): 6,
        (6, 7): 13,
        (6, 12): 33,

        (7, 9): 32,
        (7, 11): 20,

        (8, 7): 23,
        (8, 9): 11,
        (8, 10): 2,

        (9, 6): 8,
        (9, 11): 1,
        (9, 12): 10,

        (10, 12): 11,

        (11, 10): 14,
        (11, 12): 12,
    }
    state = {}
    result_flow = 0

    with open('initial.gv', 'w') as f:
        print(draw_digraph(graph, state), file=f)

    print(r"\section{Полный поток по Теореме 1}")
    print(r"\newcounter{path_counter}")
    result_flow, state = process_section(graph, result_flow, state)
    print(r"\section{Максимальный поток по Теореме 2}")

    result_flow, state = process_section(graph, result_flow, state, allow_reverse=True)
    print(f"{str(result_flow)}")

    with open('final.gv', 'w') as f:
        nodes = list(set(find_accessable(graph, state)))
        print(draw_digraph(graph, state, highlight_nodes=nodes), file=f)


def process_section(graph, result_flow, state, allow_reverse=False):
    cntr = 0
    state = state.copy()

    path = find_path(graph, state, allow_reverse=allow_reverse)
    while path is not None:
        digraph_name = f"graph_{'r' if allow_reverse else 'f'}_{cntr}.gv"

        delta = min(float('inf'), *get_positive_flow_part(graph, state, path))
        xi = min(float('inf'), *get_negative_flow_part(graph, state, path)) if allow_reverse else None

        print()
        print(r"\hline")
        print(r"\textbf{Путь " + repr_path(path) + "}")
        print(r"\stepcounter{path_counter}")

        with open(digraph_name, 'w') as f:
            nodes = list(set(find_accessable(graph, state))) if allow_reverse else None
            print(draw_digraph(graph, state, highlight_path=path,
                               highlight_nodes=nodes), file=f)

        print("""
        \\being{figure}[h]
            \\centering
            \\includegraphics[width=\\textwidth]{%s}
            \\caption{Путь "\\Alph{path_counter}" на графе}
        \\end{figure}
        """ % digraph_name)

        print(draw_formulas(graph, result_flow, path, state, delta, xi))

        if allow_reverse:
            delta = min(xi, delta)
        result_flow += delta

        new_state = state_from_apply(graph, state, path, delta)

        print(draw_fulfilled(graph, state, new_state))

        state = new_state.copy()
        path = find_path(graph, state, allow_reverse=allow_reverse)
        cntr += 1

    return result_flow, state


if __name__ == "__main__":
    main()

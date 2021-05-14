from .path import lagged_path


def wrap_digraph(string):
    # noinspection SpellCheckingInspection
    return """
    digraph G {
    rankdir=LR
            
    %s
    }
    """ % string


def draw_edges(graph, state=None, highlighted_path=None):
    if state is None:
        state = {}

    if highlighted_path is None:
        highlighted_path = []

    result = ""

    lag_path = lagged_path(highlighted_path)
    for pair, m_val in graph.items():
        val = state.get(pair, 0)
        result += f'x{str(pair[0])} -> x{str(pair[1])} [label="{str(val)}/{str(m_val)}"'
        if m_val == val:
            result += " style=bold"
        if pair in lag_path or tuple(reversed(pair)) in lag_path:
            result += " color=red"
        result += "]\n"

    if highlighted_path:
        # noinspection SpellCheckingInspection
        result += f'x{highlighted_path[0]} [xlabel=<<font color="red">+</font>>]\n'

        for pair in lag_path:
            src, cur = pair
            sign = '+' if pair in graph else '-'
            # noinspection SpellCheckingInspection
            result += f'x{str(cur)} [xlabel=<<font color="red">{sign}{str(src)}</font>>]\n'

    return result


def mark_nodes(nodes):
    result = ""
    for node in nodes:
        result += f'x{str(node)} [style=filled fillcolor=red]\n'
    return result


def draw_digraph(graph, state=None, highlight_path=None, highlight_nodes=None):
    result = ""
    result += draw_edges(graph, state, highlight_path)

    if highlight_nodes:
        result += mark_nodes(highlight_nodes)

    return wrap_digraph(result)

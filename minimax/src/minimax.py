def minimax_decision(node, skynet):
    v = -2
    visited = set()
    visited.add(node)
    for gateway in skynet.gateway_ordering(node):
        for neighbor in list(skynet.adjacency[gateway]):
            skynet.cutLink(gateway, neighbor)
            v = max(v, min_value(node, skynet, visited, 1))
            if v >= 0:
                return [gateway, neighbor]
            else:
                skynet.addLink(gateway, neighbor)
    raise Exception("You can't win")


def max_value(node, skynet, visited, depth):
    if skynet.terminalTest(node):
        return skynet.utility(node)
    if skynet.cutoffTest(node, depth):
        return 0
    v = -2
    for gateway in skynet.gateway_ordering(node):   # heuristic ordering of gateways
        for neighbor in list(skynet.adjacency[gateway]):
            skynet.cutLink(gateway, neighbor)
            v = max(v, min_value(node, skynet, visited, depth+1))
            skynet.addLink(gateway, neighbor)
            if v >= 0:
                return v    # 'static' beta pruning
    return v


def min_value(node, skynet, visited, depth):
    if skynet.terminalTest(node):
        return skynet.utility(node)
    if skynet.cutoffTest(node, depth):
        return 0
    v = 2
    for neighbor in skynet.preference(node, visited):    # heuristic ordering of nodes
        haveToRemove = neighbor not in visited
        visited.add(neighbor)
        v = min(v, max_value(neighbor, skynet, visited, depth+1))
        if haveToRemove:
            visited.remove(neighbor)
        if v == -1:
            return v    # 'static' alpha pruning
    return v

def find_set(n, s):
    for i in s:
        if n in i:
            return i

def kruskals(graph, edges):
    """Takes dictionary adjacency list of undirected graph
    and dictionary of edge weights (each undirected edge
    will be represented exactly once in arbitrary order).
    Returns total mst_weight of minimum spanning tree."""
    
    MST = {}
    S = dict(sorted(edges.items(), key = lambda n: n[1]))
    mst_weight = 0
    find_s = []

    for n in graph:
        find_s.append({n})

    for x, y in S:

        find_set_x = find_set(x, find_s)
        find_set_y = find_set(y, find_s)

        if find_set_x != find_set_y:

            find_s.remove(find_set_x)
            find_s.remove(find_set_y)
            find_s.append(find_set_x.union(find_set_y))

            mst_weight += S.get((x, y))
    
    return mst_weight
        






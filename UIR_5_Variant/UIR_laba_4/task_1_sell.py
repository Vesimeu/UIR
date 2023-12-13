network = {
    'S': {'A': 7, 'B': 4},
    'A': {'F': 5,'C':4},
    'B': {'C': 6,'D':5},
    'C': {},
    'D': {'F':1},
    'F': {}
}


def findShortestPath(start, end):
    global network
    shortest_routes = {node: float('inf') for node in network}
    shortest_routes[start] = 0
    unexplored_nodes = set(network.keys())

    while unexplored_nodes:
        current_node = min(unexplored_nodes, key=lambda node: shortest_routes[node])
        unexplored_nodes.remove(current_node)

        for neighbor, weight in network[current_node].items():
            if shortest_routes[neighbor] > shortest_routes[current_node] + weight:
                shortest_routes[neighbor] = shortest_routes[current_node] + weight

    return shortest_routes[end]


def program():
    print("Минимальная длина от S до F:\t", findShortestPath('S', 'F'))


if __name__ == "__main__":
    program()

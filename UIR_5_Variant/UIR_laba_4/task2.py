from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # Если путь не найден

# Пример использования
graph = {
    'CAB': ['CAR', 'CAT'],
    'CAR': ['CAT', 'BAR'],
    'CAT': ['MAT', 'BAT'],
    'BAR': ['MAT'],
    'MAT': ['BAT']
}

start_node = 'CAB'
end_node = 'BAT'

shortest_path = bfs(graph, start_node, end_node)

if shortest_path:
    print(f"Кратчайший путь от {start_node} до {end_node}: {shortest_path}")
else:
    print(f"Путь от {start_node} до {end_node} не найден.")

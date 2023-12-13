from collections import deque

def find_shortest_path(graph, start, end):
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
custom_graph = {
    'CAB': ['CAR', 'CAT'],
    'CAR': ['CAT', 'BAR'],
    'CAT': ['MAT', 'BAT'],
    'BAR': ['MAT'],
    'MAT': ['BAT']
}

start_point = 'CAB'
end_point = 'BAT'

result_path = find_shortest_path(custom_graph, start_point, end_point)

if result_path:
    print(f"Кратчайший путь от {start_point} до {end_point}: {result_path} | длина = {len(result_path)}")
else:
    print(f"Путь от {start_point} до {end_point} не найден.")

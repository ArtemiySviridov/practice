def find_all_paths(dictionary, current, final_point, way):
    way = way + [current]
    ways = []

    if current == final_point:
        return [way]

    if not dictionary.get(current):
        return []

    for neighbor in dictionary[current]:
        new_paths = find_all_paths(dictionary, neighbor, final_point, way)
        ways.extend(new_paths)

    return ways


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []

paths = find_all_paths(graph, start, end, path)
print("Все пути из точки A в точку F: ", *paths)

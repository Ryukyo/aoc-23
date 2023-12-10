with open("day10.txt", "r") as f:
    lines = f.readlines()

pipe_types = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}

directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

map = [[c for c in line.strip()] for line in lines]

for i in range(len(map)):
    for j in range(len(map[i])):
        place = map[i][j]
        if place == 'S':
            start = (i, j)

encountered_places = dict()

search_queue = [(start, 0)]
while len(search_queue) > 0:
    current, distance = search_queue.pop(0)
    if current in encountered_places:
        continue
    encountered_places[current] = distance
    i, j = current
    available_directions = pipe_types[map[i][j]]
    for direction in available_directions:
        di, dj, opposite = directions[direction]
        new = (i + di, j + dj)
        if i + di < 0 or i + di >= len(map):
            continue
        if j + dj < 0 or j + dj >= len(map[i + di]):
            continue
        target = map[i + di][j + dj]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite in target_directions:
            search_queue.append((new, distance + 1))

max_distance = max(encountered_places.values())


print(max_distance)
import random

def walk_to(visited_rooms, current_room):
    possible_directions = []
    directions = visited_rooms[current_room.id]

    for direction in directions.items():
        if direction[1] == '?' and direction[1] not in visited:
            possible_directions.append(direction[0])

    return random.choice(possible_directions)



visited = {
        0: {'n': '?', 's': '?', 'e': '?', 'w': '?'},
        1: {'n': '?', 's': 0, 'w': '?'},
        2: {'n': 3, 's': 1, 'w': 0},
        2: {'n': '?', 's': '?', 'w': 0},
        }

print(walk_to(visited, visited[0]))

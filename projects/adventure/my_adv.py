"""
Try one:


def walk_to(visited_rooms, current_room):
    possible_directions = []
    directions = visited_rooms[current_room.id]

    for direction in directions.items():
        if direction[1] == '?' and direction[1] not in visited:
            possible_directions.append(direction[0])

    if len(possible_directions) > 0:
        return random.choice(possible_directions)

    return None

# populate directions with ?
def initialize_directions(room):
    for direction in room.get_exits():
        visited[room.id][direction] = '?'

reverse = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

visited = {}

while len(visited) < len(world.rooms):

    cur_room = player.current_room

    if cur_room.id not in visited:
        visited[cur_room.id] = {}
        initialize_directions(cur_room)

    # could be 'w', 's', etc. or None
    cur_direction = walk_to(visited, cur_room)

    if cur_direction:
        # append direction to the path
        traversal_path.append(cur_direction)
        # find next room in that direction
        next_room = cur_room.get_room_in_direction(cur_direction)
        # mark direction in cur_room with next room id
        visited[cur_room.id][cur_direction] = next_room.id

        # in next room, mark direction from which we came
        visited[next_room.id] = {}
        initialize_directions(next_room)
        visited[next_room.id][reverse[cur_direction]] = cur_room.id

        player.current_room = next_room

"""





reverse = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# populate directions with ?
def initialize_directions(room):
    for direction in room.get_exits():
        visited[room.id][direction] = '?'

def add(room, visited):
    if room.id not in visited:
        visited[room.id] = {}

    initialize_directions(room)

def pick_direction(visited, room):
    possible_directions = []
    directions = visited[room.id]

    for direction in directions.items():
        if direction[1] == '?' and direction[1] not in visited:
            possible_directions.append(direction[0])

    if len(possible_directions) > 0:
        return random.choice(possible_directions)

    return None


visited = {}

while len(visited) < len(world.rooms):
    # Start in room 0
    room = player.current_room
    # add room to our graph
    add(room, visited)

    # pick a random unexplored direction from the player current room
    direction = pick_direction(visited, room)

    if direction:
        # log that direction
        traversal_path.append(direction)

        # get next room
        next_room = room.get_room_in_direction(direction)

        # mark direction in cur_room with next room id
        visited[room.id][direction] = next_room.id
        
        # add next room to visited and initialize directions to ?
        add(next_room, visited)

        # in next room, mark direction from which we came
        visited[next_room.id][reverse[cur_direction]] = cur_room.id

        # travel in the room
        player.current_room = next_room


        # loop

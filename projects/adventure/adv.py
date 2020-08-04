from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

"""
Start by writing an algorithm that picks a random unexplored direction from the
player's current room, travels and logs that direction, then loops.  This should
cause your player to walk a depth-first traversal.  When you reach a dead-end
(i.e. a room with no unexplored paths), walk back to the nearest room that does
contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first
search for a room with a `'?'` for an exit. If you use the `bfs` code from the
homework, you will need to make a few modifications.


player.current_room.id             # returns an integer
player.current_room.get_exits()    # returns a list: ['n', 's', 'w', 'e']
player.travel(direction)           # takes a string 'n', 's', etc.
"""

class Graph:
    def __init__(self):
        self.rooms = {}

    def add(self, room):
        if room.id not in self.rooms:
            self.rooms[room.id] = {}
        self.initialize_directions(room)

    def initialize_directions(self, room):
        for direction in room.get_exits():
            if direction not in self.rooms[room.id]:
                self.rooms[room.id][direction] = '?'

    def pick_direction(self, room):
        possible_directions = []
        directions = self.rooms[room.id]

        for direction in directions.items():
            if direction[1] == '?' and direction[1] not in self.rooms:
                possible_directions.append(direction[0])

        if len(possible_directions) > 0:
            return random.choice(possible_directions)

        return None


reverse = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}


visited = Graph()

while len(visited.rooms) < len(world.rooms):
    # Start in room 0
    room = player.current_room
    # add room to our graph
    # add(room, visited)
    visited.add(room)

    # pick a random unexplored direction from the player current room
    direction = visited.pick_direction(room)

    if direction:
        # log that direction
        traversal_path.append(direction)
        # get next room
        next_room = room.get_room_in_direction(direction)
        # mark direction in cur_room with next room id
        visited.rooms[room.id][direction] = next_room.id
        # add next room to visited and initialize directions to ?

        # add(next_room, visited)
        visited.add(next_room)

        # in next room, mark direction from which we came
        visited.rooms[next_room.id][reverse[direction]] = room.id
        # travel in the room
        player.current_room = next_room

    # When you reach a dead-end (i.e. a room with no unexplored paths), walk back
    # to the nearest room that does contain an unexplored path.
    else:
        print("player current room:", player.current_room.id)
        break









# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

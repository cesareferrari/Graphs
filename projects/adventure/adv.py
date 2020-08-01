from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
player's current room, travels and logs that direction, then loops. 
This should cause your player to walk a depth-first traversal. 
When you reach a dead-end (i.e. a room with no unexplored paths), 
walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first 
search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, 
you will need to make a few modifications.

# get_exits returns a list: ['n', 's', 'w', 'e']
"""

graph = {}  # my graph
visited = set()  # set that holds visited rooms

# while number of graph entries is less than room_graph
# while len(graph) <= len(room_graph):

current_room = player.current_room

# add current room to visited
visited.add(current_room)

# find possible directions from the current room
directions = current_room.get_exits()
# add room id to the graph
graph[current_room.id] = {}
# for each direction, add a question mark because we don't know which
# room is in that direction yet
for direction in directions:
    graph[current_room.id][direction] = '?'
# should look like this at this point
# {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}

# find directions to explore for this room
available_directions = []

for direction in graph[current_room.id].items():
    if direction[1] == '?':
        available_directions.append(direction[0])

# choose one direction randomly among the ones available
direction_to_try = random.choice(available_directions)

player.travel(direction_to_try)
# log that direction
graph[current_room.id][direction_to_try] = player.current_room.id









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

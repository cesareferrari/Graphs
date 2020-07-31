class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


# Describe in graph terminology

# 1. describe in graph terminology

# Nodes: words
# Edges: 1 letter differences

# 2. build the graph
# get_neighbors
# add vertices

# 3. choose algorithm
# BFS: shortest transformation sequence

import string

f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

def get_neighbors(word):
    neighbors = []
    # for every letter in the word
    for i in range(len(word)):
    ## for every letter in the alphabet
        for alphaletter in string.ascii_lowercase: # returns the alphabet
    ### swap out the word-letter with the alphabet-letter
            # turn into a list
            word_list = list(word)
            word_list[i] = alphaletter

            # turn the word_list back into a string
            maybe_neighbor = "".join(word_list)

            ### if the new word is in the word dictionary, then it's a neighbor
            if maybe_neighbor in word_set and maybe_neighbor != word:
                neighbors.append(maybe_neighbor)

    return neighbors



def find_ladders(start_word, end_word):
    q = Queue()
    visited = set()

    # enqueue the starting path
    q.enqueue([start_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]

        if current_node == end_word:
            return current_path

        if current_node not in visited:
            visited.add(current_node)
            
            neighbors = get_neighbors(current_node)

            for neighbor in neighbors:
                neighbor_path = current_path.copy() # or list(current_path)
                neighbor_path.append(neighbor)
                q.enqueue(neighbor_path)




print(find_ladders("hit", "cog"))
print(find_ladders("dog", "cat"))
print(find_ladders("tile", "maze"))

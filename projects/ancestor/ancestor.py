
def earliest_ancestor(ancestors, starting_node):

    # build the graph
    people = {}

    for person in ancestors:
        # establish relationship between child and parent (child has a parent)
        if person[1] not in people:
            people[person[1]] = [person[0]]
        else:
            people[person[1]].append(person[0])

    # return early if node is not found
    if starting_node not in people:
        return -1

    # starting node is current generation
    cur_gen = people[starting_node]

    while True:
        # initialize new generation list
        new_gen = []

        # if person in current generation is in people, add parent to new gen list
        for person in cur_gen:
            if person in people:
                new_gen = new_gen + people[person]
        
        if len(new_gen) == 0:
            return cur_gen[0]
        else:
            cur_gen = new_gen
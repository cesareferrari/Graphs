from util import Queue, Stack


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        # initialize a stack
        s = Stack()

        visited = set()

        # put the first node (starting_vertex) in the stack
        s.push(starting_vertex)

        # while the stack is not empty
        while s.size() > 0:
            # pop the node from the stack and put it into the `current_node` variable
            current_node = s.pop()

            # if current_node is not visited
            if current_node not in visited:
                # # mark it as visited
                visited.add(current_node)
                print(current_node)
                # # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # # put the neighbors at the top of the stack
                for neighbor in neighbors:
                    s.push(neighbor)



    def bft(self, starting_vertex):
        # make queue
        q = Queue()
        # enqueue starting vertex
        
        q.enqueue(starting_vertex)

        # track visited nodes using a set
        # initialize visited as an empty set
        visited = set()

        # look at the queue, does it still have something in it?
        while q.size() > 0:
            ## dequeue from the front, current vertex
            current_vertex = q.dequeue()

            ## if we did not visit this node
            if current_vertex not in visited:
                ### add to visited
                visited.add(current_vertex)
                print('current vertex', current_vertex)
                
                ### get its neighbors and add them to the queue
                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def bfs(self, starting_vertex, target):
        pass


    """
    Returns a list containing a path from starting vertex
    to destination vertex in depth-first order
    Use recursion
    """
    def dfs_recursive(self, current_vertex, destination_vertex, path=[], visited=None):
        if visited == None:
            visited = set()

        if current_vertex not in visited:
            visited.add(current_vertex)

        if len(path) == 0:
            path.append(current_vertex)

        if current_vertex == destination_vertex:
            return path

        neighbors = self.get_neighbors(current_vertex)

        for neighbor in neighbors:
            if neighbor not in visited:
                # recurse
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)

                if result is not None:
                    return result

        return None


if __name__ == "__main__":

    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'B')
    graph.add_edge('D', 'E')

    print(graph.vertices)
    print(graph.dft('A'))

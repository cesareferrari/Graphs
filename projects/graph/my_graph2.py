from util import Stack, Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices:
            self.vertices[from_vertex].add(to_vertex)

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]

    # depth first traversal
    def dft(self, vertex):
        s = Stack()
        visited = set()

        s.push(vertex)

        while s.size() > 0:
            current_vertex = s.pop()

            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)

                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    s.push(neighbor)

    # breadth first traversal
    def bft(self, vertex):
        q = Queue()
        visited = set()

        q.enqueue(vertex)

        while q.size() > 0:
            current_vertex = q.dequeue()

            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)

                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft_recursive(self, vertex, visited=None):
        if visited == None:
            visited = set()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            neighbors = self.get_neighbors(vertex)

            if len(neighbors) == 0:
                return visited

            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        visited = set()

        path = [starting_vertex]
        q.enqueue(path)

        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)

                    q.enqueue(neighbor_path)





if __name__ == "__main__":

    g = Graph()

    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)

    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(1, 5)
    g.add_edge(5, 3)
    g.add_edge(3, 4)

    print(g.vertices)

    print(g.bfs(1, 4))

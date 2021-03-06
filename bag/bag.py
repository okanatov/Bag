class Bag:
    class BagIterator:
        def __init__(self, collection):
            self._collection = collection
            self._pos = 0

        def __next__(self):
            if self._pos >= len(self._collection):
                raise StopIteration()

            elem = self._collection[self._pos]
            self._pos += 1

            return elem

    def __init__(self):
        self._vertices = []

    def add_edge(self, vertex, adj):
        self._try_or_create(vertex)
        self._vertices[vertex].append(adj)
        for elem in range(vertex, adj):
            self._try_or_create(adj)

    def __str__(self):
        string_representation = ""

        for vertex_index, vertex in enumerate(self._vertices):
            if vertex_index != 0:
                string_representation += "; "

            string_representation += str(vertex_index)
            string_representation += ": "
            string_representation += self._print_edges(vertex)

        return string_representation

    def _print_edges(self, vertex):
        result = ""

        for edge_index, edge in enumerate(vertex):
            if edge_index != 0:
                result += ", "
            result += str(edge)

        return result

    def is_edge(self, vertex, adj):
        for idx, vertices in enumerate(self._vertices):
            if idx is vertex and adj in vertices:
                return True

        return False

    def _try_or_create(self, index):
        try:
            self._vertices[index]
        except IndexError:
            self._vertices.insert(index, [])

    def __len__(self):
        return len(self._vertices)

    def __iter__(self):
        return self.BagIterator(self._vertices)

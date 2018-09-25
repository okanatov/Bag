import bag

class Bag:
    def __init__(self):
        self._vertices = []


    def add_edge(self, f, t):
        try: 
            self._vertices[f]
        except IndexError:
            self._vertices.insert(f, [])

        self._vertices[f].append(t)

        try: 
            self._vertices[t]
        except IndexError:
            self._vertices.insert(t, [])


    def __str__(self):
        v = ""

        for i, vertex in enumerate(self._vertices):
            v += str(i)
            v += ": "
            for edge in vertex:
                v += str(edge)
            v += "; "

        return v

import unittest
import bag

class TestBag(unittest.TestCase):
    def test_empty_bag(self):
        graph = bag.Bag()
        self.assertEqual(str(graph), "")

    def test_adds_edge(self):
        graph = bag.Bag()
        graph.add_edge(0, 1)

        self.assertEqual(str(graph), "0: 1; 1: ")

    def test_adds_edge_with_gap(self):
        graph = bag.Bag()
        graph.add_edge(0, 4)
        graph.add_edge(1, 2)
        graph.add_edge(0, 6)

        self.assertEqual(str(graph), "0: 4, 6; 1: 2; 2: ; 3: ; 4: ; 5: ; 6: ")

    def test_adds_2_edges(self):
        graph = bag.Bag()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        self.assertEqual(str(graph), "0: 1, 2; 1: 2; 2: ")

    def test_gets_length(self):
        graph = bag.Bag()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        self.assertEqual(len(graph), 3)

    def test_iterates(self):
        graph = bag.Bag()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        iterator = iter(graph)

        self.assertEqual(str(next(iterator)), str([1, 2]))
        self.assertEqual(str(next(iterator)), str([2]))
        self.assertEqual(str(next(iterator)), str([]))

    def test_raises_stop_iteration(self):
        graph = bag.Bag()
        graph.add_edge(0, 1)

        iterator = iter(graph)
        next(iterator)
        next(iterator)

        self.assertRaises(StopIteration, next, iterator)

    def test_checks_whether_edge_present(self):
        graph = bag.Bag()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)

        self.assertTrue(graph.is_edge(0, 2))
        self.assertFalse(graph.is_edge(1, 2))
        self.assertFalse(graph.is_edge(0, 3))
        self.assertFalse(graph.is_edge(0, 0))

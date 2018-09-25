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

    def test_adds_2_edges(self):
        graph = bag.Bag()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        self.assertEqual(str(graph), "0: 1, 2; 1: 2; 2: ")

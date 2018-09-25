import unittest
import bag

class TestBag(unittest.TestCase):

    def test_empty_bag(self):
        b = bag.Bag()
        self.assertEqual(str(b), "")

    def test_adds_edge(self):
        b = bag.Bag()
        b.add_edge(0, 1)

        self.assertEqual(str(b), "0: 1; 1: ; ")

import unittest
from shortest_chain_of_friends import *


class TestNetwork(unittest.TestCase):
    def test_shortest_chain_of_friends(self):
        network = {'A': ['B', 'C'],
                   'B': ['A', 'D', 'E'],
                   'C': ['A', 'F', 'G'],
                   'D': ['B', 'E', 'F'],
                   'E': ['B', 'F', 'H'],
                   'F': ['C', 'D', 'E'],
                   'G': ['C', 'H'],
                   'H': ['G', 'E']
                   }
        self.assertAlmostEqual(shortest_chain_of_friends(network, 'A', 'G'),
                               2)  # diferite teste in care rezultatul este corect
        self.assertAlmostEqual(shortest_chain_of_friends(network, 'A', 'H'), 3)
        self.assertAlmostEqual(shortest_chain_of_friends(network, 'A', 'A'), 0)
        network = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A'],
            'D': []
        }
        self.assertAlmostEqual(shortest_chain_of_friends(network, 'A', 'D'), -1)  # un test in care avem un nod izolat

        network = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': ['A', 'H'],
            'D': []
        }
        self.assertRaises(ValueError, shortest_chain_of_friends, network, 'A',
                          'D')  # un test in care avem un nod in lista de vecini care nu exista in graf

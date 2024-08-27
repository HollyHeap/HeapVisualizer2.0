# tests/test_heaps.py
import unittest
from heap_visualizer import visualize_heap

class TestHeapVisualizer(unittest.TestCase):
    def test_visualize_heap(self):
        data = [5, 7, 9, 1, 3]
        expected = [1, 3, 5, 7, 9]
        heap = visualize_heap(data)
        self.assertEqual(heap, expected)

if __name__ == "__main__":
    unittest.main()

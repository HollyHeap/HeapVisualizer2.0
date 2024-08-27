# tests/test_heaps.py
import unittest
from heap_visualizer import visualize_heap
from utilities.heap_utils import merge_heaps, find_min

class TestHeapVisualizer(unittest.TestCase):
    def test_visualize_heap(self):
        data = [5, 7, 9, 1, 3]
        expected = [1, 3, 5, 7, 9]
        heap = visualize_heap(data)
        self.assertEqual(heap, expected)

    def test_merge_heaps(self):
        heap1 = [1, 3, 5, 7, 9]
        heap2 = [2, 4, 6, 8, 10]
        merged = merge_heaps(heap1, heap2)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(merged, expected)

    def test_find_min(self):
        heap = [1, 3, 5, 7, 9]
        self.assertEqual(find_min(heap), 1)

    def test_find_min_empty(self):
        heap = []
        self.assertIsNone(find_min(heap))

if __name__ == "__main__":
    unittest.main()

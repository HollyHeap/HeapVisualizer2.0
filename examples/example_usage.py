# examples/example_usage.py
from heap_visualizer import visualize_heap
from utilities.heap_utils import merge_heaps, find_min

data1 = [5, 7, 9, 1, 3]
data2 = [2, 4, 6, 8, 10]

# This needs to be done before merging

heap1 = visualize_heap(data1)
heap2 = visualize_heap(data2)

merged_heap = merge_heaps(heap1, heap2)
print("Merged Heap:", merged_heap)
print("Minimum:", find_min(merged_heap))

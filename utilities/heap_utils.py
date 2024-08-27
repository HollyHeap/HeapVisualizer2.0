# utilities/heap_utils.py
def merge_heaps(heap1, heap2):
    combined = heap1 + heap2
    heapq.heapify(combined)
    return combined

def find_min(heap):
    if heap:
        return heap[0]
    return None

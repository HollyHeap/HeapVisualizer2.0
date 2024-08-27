# heap_visualizer.py
import heapq

def visualize_heap(data):
    heapq.heapify(data)
    return data

if __name__ == "__main__":
    data = [5, 7, 9, 1, 3]
    heap = visualize_heap(data)
    print("Heap:", heap)

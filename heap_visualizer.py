# heap_visualizer.py
import heapq
import logging

logging.basicConfig(level=logging.INFO, filename='heap.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

def visualize_heap(data):
    heapq.heapify(data)
    logging.info(f"Heapified data: {data}")
    return data

if __name__ == "__main__":
    data = [5, 7, 9, 1, 3]
    heap = visualize_heap(data)
    print("Heap:", heap)

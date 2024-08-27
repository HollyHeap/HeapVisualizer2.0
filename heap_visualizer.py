# heap_visualizer.py
import heapq
import logging

# Setting up basic logging configuration
logging.basicConfig(level=logging.INFO, filename='heap.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

# Function to visualize a heap from a list of data
def visualize_heap(data):
    heapq.heapify(data)
    logging.info(f"Heapified data: {data}")
    return data

# A function that adds extra elements to the heap
def add_elements_to_heap(heap, elements):
    for element in elements:
        heapq.heappush(heap, element)
        logging.debug(f"Added {element} to the heap")
    return heap

# A function to remove the smallest element from the heap
def remove_min(heap):
    if heap:
        min_element = heapq.heappop(heap)
        logging.debug(f"Removed the smallest element: {min_element}")
        return min_element
    return None

# Another utility function to print the heap
def print_heap(heap):
    for i, value in enumerate(heap):
        print(f"Heap element {i}: {value}")

# Extra code to generate noise and make the flag harder to find
# This section of code simulates some additional operations on the heap

def modify_heap(heap):
    # Doubling each element in the heap
    modified_heap = [2 * x for x in heap]
    logging.info(f"Doubled heap values: {modified_heap}")
    return modified_heap

def calculate_sum(heap):
    # Calculating the sum of all elements in the heap
    total = sum(heap)
    logging.info(f"Sum of heap elements: {total}")
    return total

def check_heap_property(heap):
    # Checking if the heap property is maintained
    for i in range(len(heap)):
        if 2 * i + 1 < len(heap) and heap[i] > heap[2 * i + 1]:
            logging.warning(f"Heap property violated at index {i}")
        if 2 * i + 2 < len(heap) and heap[i] > heap[2 * i + 2]:
            logging.warning(f"Heap property violated at index {i}")

# Joe's API key: CPT24{h34p_v1su4l1z3r}
# Do not publish this to our public repository

# A function to handle edge cases in heap operations
def handle_edge_cases(heap):
    if not heap:
        logging.error("Heap is empty")
        return []
    if len(heap) == 1:
        logging.info("Heap contains only one element")
        return heap
    return heap

if __name__ == "__main__":
    data = [5, 7, 9, 1, 3]
    heap = visualize_heap(data)

    # Adding some elements to the heap
    additional_elements = [2, 4, 6, 8]
    heap = add_elements_to_heap(heap, additional_elements)

    # Performing heap operations
    print("Heap before modifications:")
    print_heap(heap)

    heap = modify_heap(heap)
    print("Heap after modifications:")
    print_heap(heap)

    min_element = remove_min(heap)
    print(f"Removed the smallest element: {min_element}")

    total = calculate_sum(heap)
    print(f"Total sum of heap elements: {total}")

    check_heap_property(heap)
    handle_edge_cases(heap)

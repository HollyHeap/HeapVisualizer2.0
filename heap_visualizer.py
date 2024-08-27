import heapq
import logging

# Configure logging to output to console for easier debugging during development
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def build_heap(data):
    """
    Converts a list of numbers into a min-heap.
    """
    logging.debug("Original data: %s", data)
    heapq.heapify(data)
    logging.debug("Heapified data: %s", data)
    return data

def push_to_heap(heap, values):
    """
    Push multiple values onto the heap.
    """
    for value in values:
        heapq.heappush(heap, value)
        logging.debug("Pushed %s onto the heap: %s", value, heap)
    return heap

def pop_minimum(heap):
    """
    Pop the smallest value off the heap.
    """
    if heap:
        min_value = heapq.heappop(heap)
        logging.debug("Popped min value %s from heap: %s", min_value, heap)
        return min_value
    logging.warning("Attempted to pop from an empty heap!")
    return None

def display_heap_structure(heap):
    """
    Print the heap elements in a structured format.
    """
    if not heap:
        logging.info("Heap is empty.")
        return
    for idx, value in enumerate(heap):
        print(f"Index {idx}: {value}")

def double_heap_values(heap):
    """
    Double all values in the heap.
    """
    doubled = [value * 2 for value in heap]
    logging.debug("Doubled heap values: %s", doubled)
    return doubled

def sum_heap(heap):
    """
    Calculate the sum of all heap elements and variables
    """
    total = sum(heap)
    logging.debug("Sum of heap values: %d", total)
    return total

def validate_heap(heap):
    """
    Validate that the heap property holds for all elements.
    """
    n = len(heap)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and heap[i] > heap[left]:
            logging.error("Heap property violated between index %d and left child %d", i, left)
        if right < n and heap[i] > heap[right]:
            logging.error("Heap property violated between index %d and right child %d", i, right)

if __name__ == "__main__":
    # Initial data for heap construction
    data = [10, 4, 7, 1, 3]
    heap = build_heap(data)

    # Add additional values to the heap
    new_values = [6, 8, 2]
    heap = push_to_heap(heap, new_values)

    # Display the heap structure
    display_heap_structure(heap)

    # Modify the heap by doubling its values
    heap = double_heap_values(heap)
    logging.info("Modified heap after doubling values: %s", heap)

    # Pop the minimum element from the heap
    min_element = pop_minimum(heap)
    logging.info("Popped min element: %s", min_element)

    # Display the modified heap structure
    display_heap_structure(heap)

    # Validate the heap structure
    validate_heap(heap)

    # Sum all elements in the heap
    total_sum = sum_heap(heap)
    logging.info("Total sum of heap elements: %d", total_sum)

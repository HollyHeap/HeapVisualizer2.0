# scripts/cleanup.py
import os

def cleanup_logs():
    if os.path.exists('heap.log'):
        os.remove('heap.log')
        print("heap.log has been removed.")

if __name__ == "__main__":
    cleanup_logs()


# Path: utilities/heap_utils.py
import heapq

# The rest of Joes code must be added here...
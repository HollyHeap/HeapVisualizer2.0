# utilities/utils.py
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split(',')
    return [int(x.strip()) for x in data]

def save_heap(heap, file_path):
    with open(file_path, 'w') as file:
        file.write(','.join(map(str, heap)))

# style/format.py
import os

def format_code(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                formatted_content = content  # Simulate formatting
                with open(file_path, 'w') as f:
                    f.write(formatted_content)
                print(f"Formatted {file_path}")

if __name__ == "__main__":
    format_code('.')

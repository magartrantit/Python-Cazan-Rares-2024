import os
import sys

def calculate_total_size(directory_path):
    total_size = 0
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")

        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except OSError as e:
                    print(f"Could not access file '{file_path}': {e}")

        print(f"Total size of all files in '{directory_path}': {total_size} bytes")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculate_size.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    calculate_total_size(directory)

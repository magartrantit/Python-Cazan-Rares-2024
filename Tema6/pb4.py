import os
import sys
from collections import defaultdict

def count_files_by_extension(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")

        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

        if not files:
            print(f"The directory '{directory_path}' is empty.")
            return

        extension_count = defaultdict(int)

        for file in files:
            _, extension = os.path.splitext(file)
            if extension:  # Exclude files without extensions
                extension_count[extension] += 1

        print(f"File counts by extension in '{directory_path}':")
        for extension, count in extension_count.items():
            print(f"{extension}: {count}")

    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print(f"Permission denied to access the directory '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_extensions.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    count_files_by_extension(directory)

import os
import sys

def rename_files_sequentially(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

        if not files:
            print(f"No files found in directory '{directory_path}'.")
            return

        files.sort()

        for index, file_name in enumerate(files, start=1):
            old_path = os.path.join(directory_path, file_name)
            file_extension = os.path.splitext(file_name)[1]
            new_name = f"file{index}{file_extension}"
            new_path = os.path.join(directory_path, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed '{file_name}' to '{new_name}'.")
            except Exception as e:
                print(f"Failed to rename '{file_name}': {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rename_files.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    rename_files_sequentially(directory)

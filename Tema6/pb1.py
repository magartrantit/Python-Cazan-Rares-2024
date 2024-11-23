import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    if not file_extension.startswith('.'):
        print("Error: File extension must start with a '.' (e.g., '.txt').")
        sys.exit(1)

    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        matching_files = [
            f for f in os.listdir(directory_path)
            if f.endswith(file_extension) and os.path.isfile(os.path.join(directory_path, f))
        ]

        if not matching_files:
            print(f"No files with extension '{file_extension}' found in directory '{directory_path}'.")
            sys.exit(0)

        for file in matching_files:
            file_path = os.path.join(directory_path, file)
            try:
                with open(file_path, 'r') as f:
                    print(f"Contents of '{file}':\n")
                    print(f.read())
                    print("-" * 40)
            except Exception as e:
                print(f"Error reading file '{file_path}': {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

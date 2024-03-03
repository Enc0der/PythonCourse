import sys

def main():
    # If a file is provided, read lines from the file
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as file:
                for i, line in enumerate(file, start=1):
                    print(f"{i}\t{line}", end='')  # Print line number and line content
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
    else:
        # If no file is provided, read lines from stdin
        for i, line in enumerate(sys.stdin, start=1):
            print(f"{i}\t{line}", end='')

if __name__ == "__main__":
    main()

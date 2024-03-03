import sys

def tail(filename=None, lines=10):
    # Function to print the last n lines from a file or stdin
    try:
        if filename:  # If a filename is specified, read lines from the file
            with open(filename, 'r') as file:
                content = file.readlines()
        else:  # If no file is specified, read lines from stdin
            content = sys.stdin.readlines()
        
        # Print the last n lines
        for line in content[-lines:]:
            print(line, end='')
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Number of lines to print is always 10, regardless of the source
    lines = 10

    # If files are provided, process each file
    if len(sys.argv) > 1:
        for i, filename in enumerate(sys.argv[1:], start=1):
            if len(sys.argv) > 2:  # If more than one file is provided, print the file name
                print(f"==> {filename} <==")
            tail(filename, lines)
            if i < len(sys.argv) - 1:  # If this is not the last file, print a separator
                print()
    else:
        # If no files are provided, read from stdin
        tail(lines=lines)

if __name__ == "__main__":
    main()

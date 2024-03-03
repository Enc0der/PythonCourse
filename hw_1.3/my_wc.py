import sys

def count_stats(filename):
    # Function to count lines, words, and characters
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        return num_lines, num_words, num_chars
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0, 0  # Return zero statistics in case of an error

def main():
    # Check if files were passed in command line arguments
    if len(sys.argv) > 1:
        total_lines, total_words, total_chars = 0, 0, 0
        for filename in sys.argv[1:]:
            num_lines, num_words, num_chars = count_stats(filename)
            print(f"{num_lines} {num_words} {num_chars} {filename}")
            total_lines += num_lines
            total_words += num_words
            total_chars += num_chars
        # Output total statistics if there were multiple files
        if len(sys.argv) > 2:
            print(f"{total_lines} {total_words} {total_chars} total")
    else:
        # If no files were provided, print instructions
        print("Usage: python my_wc.py <file1> <file2> ...")

if __name__ == "__main__":
    main()

**Python CLI Utilities**

This repository contains three Python scripts that serve as Command Line Interface (CLI) utilities. These scripts are designed to perform various file operations directly from the command line. Below is a brief overview of each script:

1. *my_nl.py*: This script is a simplified version of the `nl` utility. It reads input from a file or stdin and outputs numbered lines to stdout. If no file is provided, it reads from stdin.

2. *my_tail.py*: Similar to the `tail` utility, this script outputs the last 10 lines of each specified file to stdout. If multiple files are provided, it prints the name of each file before its output. If no files are provided, it prints the last 17 lines from stdin.

3. *my_wc.py*: This script replicates the functionality of the `wc` utility when called without additional options. It outputs statistics (number of lines, words, and characters) for each provided file, along with the filename. If multiple files are provided, it also prints the total statistics at the end.

**Usage:**

Each script can be executed directly from the command line. Below are examples of how to use each script:

- `python my_nl.py alice.txt`: Number and print lines from the specified file.
- `python my_tail.py alice.txt`: Output the last 10 lines of each file, with filenames.
- `python my_wc.py alice.txt`: Display line, word, and character count for each file, along with totals.

#coding
import sys

# Program to count command-line arguments
def main():
    num_args = len(sys.argv) - 1
    print(f"Number of arguments provided: {num_args}")

if __name__ == "__main__":
    main()
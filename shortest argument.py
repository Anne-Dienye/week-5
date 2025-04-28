#coding
import sys

# Program to find the shortest argument
def main():
    if len(sys.argv) <= 1:
        print("No arguments provided.")
        return
    
    # Exclude the program name and sort arguments by length
    args = sys.argv[1:]
    shortest = min(args, key=len)
    print(f"The shortest argument is: {shortest}")

if __name__ == "__main__":
    main()
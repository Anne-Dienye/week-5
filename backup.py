#coding
import sys
import shutil

# Program to create a backup copy of a file
def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <filename>")
        return
    
    original_file = sys.argv[1]
    backup_file = original_file + ".bak"
    
    try:
        shutil.copyfile(original_file, backup_file)
        print(f"Backup created successfully: {backup_file}")
    except FileNotFoundError:
        print(f"Error: The file '{original_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
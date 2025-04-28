#coding
import sys

# Program to process temperatures from command-line arguments
def main():
    if len(sys.argv) <= 1:
        print("No temperature values provided.")
        return
    
    try:
        temperatures = [float(temp) for temp in sys.argv[1:]]
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        print(f"Maximum: {max_temp}, Minimum: {min_temp}, Mean: {mean_temp:.2f}")
    except ValueError:
        print("Invalid input. Please provide numeric temperature values.")

if __name__ == "__main__":
    main()
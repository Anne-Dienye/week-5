#coding
import sys
import requests

# Program to check if a website exists
def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <URL>")
        return
    
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} returned status code {response.status_code}.")
    except requests.RequestException:
        print(f"Failed to connect to {url}. The website may not exist.")

if __name__ == "__main__":
    main()
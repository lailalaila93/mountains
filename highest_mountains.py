# List of the world's tallest mountains with their heights (in meters)
import time

mountains = [
    {"name": "Mount Everest", "height": 8848},
    {"name": "K2", "height": 8611},
    {"name": "Kangchenjunga", "height": 8586},
    {"name": "Lhotse", "height": 8516},
    {"name": "Makalu", "height": 8485},
    {"name": "Cho Oyu", "height": 8188},
    {"name": "Dhaulagiri", "height": 8167},
    {"name": "Manaslu", "height": 8163},
    {"name": "Nanga Parbat", "height": 8126},
    {"name": "Annapurna", "height": 8091},
]

# Function to display the list of highest mountains
def display_mountains(mountains):
    print("The World's Tallest Mountains:")
    for mountain in mountains:
        print(f"{mountain['name']} - {mountain['height']} m")

# Main function to run the script
def main():
    print("Highest Mountains - A List of the World's Tallest Mountains")
    display_mountains(mountains)

if __name__ == "__main__":
    main()

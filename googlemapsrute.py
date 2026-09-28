import json
import webbrowser
import urllib.parse

# Take input from terminal
source = input("Enter source: ")
destination = input("Enter destination: ")

# Store source and destination in JSON format
route = {
    "source": source,
    "destination": destination
}

# Save data to JSON file
with open("route.json", "w") as file:
    json.dump(route, file, indent=4)

# Create Google Maps direction URL
source_encoded = urllib.parse.quote(source)
destination_encoded = urllib.parse.quote(destination)

maps_url = (
    f"https://www.google.com/maps/dir/?api=1"
    f"&origin={source_encoded}"
    f"&destination={destination_encoded}"
)

# Open Google Maps in the default browser
webbrowser.open(maps_url)

print("\nRoute information saved in route.json")
print("Opening Google Maps...")
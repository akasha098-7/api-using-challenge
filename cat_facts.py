import requests

# API endpoint
url = "https://catfact.ninja/fact"

# Send GET request to fetch data
response = requests.get(url)

# Convert response to JSON format
data = response.json()

# Print the cat fact
print("🐱 Random Cat Fact 🐱")
print(data["fact"])

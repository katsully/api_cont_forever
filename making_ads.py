import requests

met_url = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"

met_data = {
    "q": "George Washington",
    "medium": "Paintings"
}

response = requests.get(met_url, data=met_data)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("BROKEN")
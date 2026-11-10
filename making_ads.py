import requests

met_url = "https://collectionapi.metmuseum.org/public/collection/v1.1/search"

met_data = {
    "q": "George Washington",
    "medium": "Paintings"
}

response = requests.get(met_url, data=met_data)
if response.status_code == 200:
    data = response.json()
    object_id = data['objectIDs'][0]
    print(object_id)
else:
    print("BROKEN")

# this will give me info about a painting using the object ID
met_url2 = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"

response2 = requests.get(met_url2)
if response2.status_code == 200:
    data2 = response2.json()
    title = data2['title']
    artist = data2['artistDisplayName']
else:
    print("BROKEN")

print(title)
print(artist)


meme_url = "https://api.imgflip.com/get_memes"
meme_response = requests.get(meme_url)
if meme_response.status_code == 200:
    meme_data = meme_response.json()
    meme_name = meme_data['data']['memes'][0]['name']
else:
    print("meme url is BROKEN")

print(meme_name)

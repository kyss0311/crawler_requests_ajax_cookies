import urllib.request as request
import json
src = "https://data.ntpc.gov.tw/api/datasets/b3a30a19-4b89-4da2-8d99-18200dc5dfde/json?page=0&size=100"
with request.urlopen(src) as response:
    data = json.load(response)
print(data)
with open("tourist_spots_data.txt","w",encoding="utf-8") as file:
    for item in data:
        file.write(item['Name'] + "\n")

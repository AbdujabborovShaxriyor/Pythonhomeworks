from bs4 import BeautifulSoup
import requests
import json
response = requests.get("https://www.demoblaze.com/")
soup = BeautifulSoup(response.text,'html.parser')

data = []
laptops = soup.find_all("div",class_="card-block")
for laptop in laptops:
    laptop_name = laptop.find("a").text
    price = laptop.find("h5").text
    laptop_description = laptop.find("p").text
    data.append({
        "name": laptop_name,
        "price": price,
        "description": laptop_description
    })
    with open("file.json","w",encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
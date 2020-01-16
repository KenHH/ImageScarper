import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# Scarping images from the first page of Bing image seaarch
search = input("Search for:")
params = {"q": search}

# Opens the connection and downloads html page from url
uClient = requests.get("http://www.bing.com/images/shearch", params=params)

# Parses html into a soup data structure to traverse html
# As if it were a json data type.
soup = BeautifulSoup(uClient.text, "html.parser")

# what class the images are stored as
links = soup.findAll("a", {"class": "thumb"})


for item in links:

    img_obj = requests.get(item.attrs["href"])
    print("Getting", item.attrs["href"])

    # Getting the last item in the list using [-1]
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./Scraped_images/" + title, img.format)

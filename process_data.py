import requests
from bs4 import BeautifulSoup

url = "https://www.hackthebox.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting data
for item in soup.select(".item", limit=5):
    title = item.find("h2").text
    link = item.find("a")["href"]
    print(f"{title}: {link}")
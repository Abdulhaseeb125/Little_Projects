import bs4 as bs
import requests

URL = "https://www.modernlibrary.com/top-100/100-best-novels/"
response = requests.get(URL)
response.raise_for_status()
data = response.text
soup = bs.BeautifulSoup(data, "html.parser")
content = soup.select(".list-100 ol .row li")
books_list = [f"{item}- {content[item].text}" for item in range(len(content))]
print(books_list)

with open("books.txt", "w") as file:
    for item in books_list:
        file.write(f"{item}\n")

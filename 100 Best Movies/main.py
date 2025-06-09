from bs4 import BeautifulSoup
import requests
import html
link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=link)
read = response.text

soup = BeautifulSoup(read, "html.parser")

movie_text = soup.find_all(name="h3", class_="title")
for rankings in movie_text[::-1]:
    movie_titles = rankings.getText()
    with open("TOP 100 MOVIES.txt", mode="w", encoding="utf8") as movies:
        movies.write(f"{html.unescape(movie_titles)}\n")


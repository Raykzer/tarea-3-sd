import requests
import os
import json
import wikipediaapi

paginas = [
    "United States Senate", 
    "Wiki", 
    "Facebook",
    "United States",
    "Donald Trump",
    "Wikipedia",
    "HTTP 404",
    "Elizabeth II",
    "Google",
    "India",
    "Barack Obama",
    "Cristiano Ronaldo",
    "World War II",
    "United Kingdom",
    "Michael Jackson",
    "Elon Musk",
    "Lady Gaga",
    "World War I",
    "The Beatles",
    "Canada",
    "Freddie Mercury",
    "List of presidents of the United States",
    "Stephen Hawking",
    "List of highest-grossing films",
    "China",
    "Russia",
    "Japan",
    "Chernobyl disaster",
    "Israel",
    "Earth"
]

def search(folder, page_title, number):
    wiki = wikipediaapi.Wikipedia(user_agent='TareaSD', language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    page = wiki.page(page_title)
    if page.exists():
        text = '{} {}<splittername>{}'.format(number, page.fullurl, json.dumps(page.text))
        filepath = f"./{folder}/articulo{number}.txt"

        if os.path.isfile(filepath):
            os.remove(filepath)

        with open(filepath, "wb") as file:
            file.write(text.encode('utf-8'))

i = 1
for pagina in paginas:
    if i <= 15:
        search('carpeta1', pagina, i)
    else:
        search('carpeta2', pagina, i)
    i += 1
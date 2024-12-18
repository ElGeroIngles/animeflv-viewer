import requests
from merge_media import merge
import sys
sys.stdout.reconfigure(encoding='utf-8')

if __name__ == "__main__":
    title = input("Name of the amime: ")

    print("Searching for animes with a similar name...")
    print("[----------]")
    searchs = requests.get(f"https://animeflv.ahmedrangel.com/api/search?query={title}&page=1").json()

    media = merge(searchs, title)

    i = 0
    for x in media:
        print(f"[{i}] " + x['title'])
        i += 1

    print(len(media))

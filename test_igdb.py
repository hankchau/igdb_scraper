import requests
import igdb_scraper


def main():
    url = 'https://api-v3.igdb.com/games'

    headers = {
        'Accept': 'application/json',
        'user-key': '56d1bc79a1da0e6bb3a3b3aef6d481a9'
    }
    body = 'fields keywords,slug; where slug="super-mario-bros"; '

    req = requests.get(url, headers=headers, data=body)
    data = req.json()

    for entry in data:
        name = igdb_scraper.sanitize_string(entry['name'])
        print(name)


if __name__ == '__main__':
    main()
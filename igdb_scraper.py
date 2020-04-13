import requests
import unidecode
import pandas as pd
import re
import string


def get_game_titles(filename):
    df = pd.read_csv(filename)
    game_titles = df['Name']

    return game_titles


def get_data(url, game_titles):
    headers = {
        'Accept': 'application/json',
        'user-key': '56d1bc79a1da0e6bb3a3b3aef6d481a9'
    }
    fields = 'limit 500; fields age_ratings,aggregated_rating,aggregated_rating_count,alternative_names,artworks,bundles,category,collection,cover,created_at,dlcs,expansions,external_games,first_release_date,follows,franchise,franchises,game_engines,game_modes,genres,hypes,involved_companies,keywords,multiplayer_modes,name,parent_game,platforms,player_perspectives,popularity,pulse_count,rating,rating_count,release_dates,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,time_to_beat,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;'

    search_results = []
    for title in game_titles:
        title = sanitize_string(title)

        search = 'search "' + title + '"; '
        body = search + fields
        req = requests.get(url, headers=headers, data=body)
        data = req.json()

        found = False
        for entry in data:
            name = sanitize_string(entry['name'])

            if name == title or name in title or title in name:
                search_results.append(entry)
                found = True
                break

        if not found:
            print(title + ' not found ... ')

    return search_results


def sanitize_string(string):
    # remove punctuations
    string = (unidecode.unidecode(string)).lower()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    string_cpy = string

    for c in string_cpy:
        if c in punctuations:
            if c == '/':
                words = string.split('/')
                return words[0]
            else:
                string = string.replace(c, " ")

    return string


def save_file(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename)


def main():
    game_titles = get_game_titles('vgsales.csv')

    url = 'https://api-v3.igdb.com/games'

    print('making API calls to IGDB ...')
    search_results = get_data(url, game_titles)

    print('saving search results to csv ...')
    save_file(search_results, 'igdb_data.csv')
    print('take a break !')


if __name__ == '__main__':
    main()
import pandas as pd
import string
import re

from bs4 import BeautifulSoup
from selenium import webdriver



def read_data(filename):
    """Reads a csv file as into a pandas dataframe."""
    return pd.read_csv(filename)


def start_driver(wait_time):
    driver = webdriver.Chrome("/Users/HankChau/Desktop/eecs499/ProjectZeta/chromedriver")
    driver.implicitly_wait(wait_time)

    return driver


def get_tags(url, game_titles):
    """Search Wikipedia for game info."""
    game_dict = {}

    driver = start_driver(3)

    for title in game_titles:
        try:
            # remove punctuations
            re.sub(string.punctuation, '', title)
            token = '-'.join(title.split())

            driver.get(url + token)
            driver.find_element_by_link_text('Read More').click()

            soup = BeautifulSoup(driver.page_source, 'lxml')

            # date
            date = soup.find('h2', '{"class": "banner-subheading"}').text

            # genre
            genre_elms = soup.find('span', string='Genre: ').find_next_siblings('a')
            genre = []
            for g in genre_elms:
                genre.append(g.string)

            # platforms
            plat_elms = soup.find('span', string='Platforms: ').find_next_siblings('a')
            platforms = []
            for p in plat_elms:
                platforms.append(p.string)

            # themes
            themes_elms = soup.find('')
            themes = []
            for t in themes_elms:
                themes.append(t.string)

            # keywords
            key_elms = soup.find('')
            keywords = []

            game_dict[title] = {
                'date': date,
                'genre': genre,
                'description': description,
                'platforms': platforms,
                'themes': themes,
                'keywords': keywords
            }

        except requests.HTTPError:
            print('HTTP Error on game: ' + title)
            continue


def main():
    df = read_data('vgsales.csv')
    game_titles = df['Name']

    url = 'https://igdb.com/games/'
    game_dictionary = get_tags(url, game_titles)





if __name__ == '__main__':
    main()
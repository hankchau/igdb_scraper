import argparse
import unidecode
import csv
import string


parser = argparse.ArgumentParser()
parser.add_argument('--key', dest='key', default='56d1bc79a1da0e6bb3a3b3aef6d481a9', help='API Access Key')
parser.add_argument('--infile', dest='infile', default='', help='Input CSV file of games')
parser.add_argument('--criteria', dest='criteria', default='*', help='A string of fields to retrieve from DB')
parser.add_argument('--limit', dest='limit', default='', help='The limit of entries retrieved')

args = parser.parse_args()


def read_csv():
    if args.infile != '':
        with open(args.infile) as f:
            reader = csv.reader(f)
            game_titles = list(reader)
        return game_titles

    print('please provide a list of games in a csv file')
    exit(0)


def sanitize_name(name):
    table = str.maketrans('', '', string.punctuation)
    name = (unidecode.unidecode(name)).lower()

    return name.translate(table)


def main():
    game_titles = read_csv()

    name2keys = {}
    keywords = {}
    unavail = []

    for i in range(len(game_titles)):
        name = sanitize_name(game_titles[i])
        slug = '-'.join(name.split())

        name2keys[name] = []

        fields = ''


if __name__ == '__main__':
    main()

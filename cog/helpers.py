from discord import Color
from random import choice
from json import loads


with open('databases/db_str.json', encoding='utf8') as strings_database:
    all_strings = strings_database.read()
    strings = loads(all_strings)

with open('databases/db_gifs.json') as gifs_database:
    all_gifs = gifs_database.read()
    gifs = loads(all_gifs)


def rbColor():
    """Returns one of the main colors of RoboTito."""
    colors = [Color.from_rgb(255, 94, 43),
              Color.from_rgb(82, 92, 253),
              Color.from_rgb(72, 159, 181),
              Color.from_rgb(255, 134, 0)]
    return choice(colors)

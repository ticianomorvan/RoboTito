import random
import json
import tomli
import discord


def open_str():
    with open('databases/db_str.json', encoding='utf8') as f:
        data = f.read()
        string = json.loads(data)
        return string


string = open_str()


def rbColor():
    colors = [discord.Color.from_rgb(255, 94, 43),
              discord.Color.from_rgb(82, 92, 253),
              discord.Color.from_rgb(72, 159, 181),
              discord.Color.from_rgb(255, 134, 0)
              ]
    return random.choice(colors)

# Functions used in cog/anime.py


def gif(string):
    with open('databases/db_gifs.json') as f:
        data = f.read()
        gif = json.loads(data)
        return random.choice(gif[string])


def header(table):
    header = open_str()[table]
    return random.choice(header)


def sentence(author, msg, member=None):
    if member is None:
        message = random.choice(string[msg])
        result = author + message
        return result
    else:
        message = random.choice(string[msg])
        result = author + message + member
        return result


def same_user(activity):
    message = 'Trata de ' + activity + ' alguien más.'
    return message


def get_embed(type: str, author, member=None):
    if member is not None:
        e = discord.Embed(color=rbColor())
        e.add_field(name=header(f'h_{type}'),
                    value=sentence(author, f'm_{type}', member))
        e.set_image(url=gif(type))
        return e
    else:
        e = discord.Embed(color=rbColor(),)
        e.add_field(name=header(f'h_{type}'),
                    value=sentence(author, f'm_{type}'))
        e.set_image(url=gif(type))
        return e


# Functions used in cog/commands.py


def get_8ball():
    return random.choice(string['ball8'])


def get_penis(number: int):
    if number >= 1:
        return random.choice(string['penis'])
    else:
        pass


def get_love(number: int):
    if number >= 75:
        return random.choice(string['love_high'])
    elif number >= 45:
        return random.choice(string['love_medium'])
    else:
        return random.choice(string['love_low'])


def get_love_gif(number: int):
    with open('databases/db_gifs.json', encoding='utf-8') as f:
        gifData = f.read()
        gifstring = json.loads(gifData)
        if number >= 65:
            gif = random.choice(gifstring['love_high'])
            return gif
        else:
            gif = random.choice(gifstring['love_low'])
            return gif


# REST API's Token


def get_api():
    with open('databases/config.toml', encoding='utf-8') as f:
        token_data = tomli.load(f)
        token = token_data['api']
        return token

import random

import json

from discord.ext import commands


def open_str():
    with open('databases/db_str.json', encoding='utf8') as f:
        data = f.read()
        string = json.loads(data)
        return string


string = open_str()


class Functions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def gif(database):
        with open('databases/db_gifs.json') as f:
            data = f.read()
            gif = json.loads(data)
            return random.choice(gif[database])

    def header(table):
        header = string[table]
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

    def sameUser(activity):
        message = 'Trata de ' + activity + ' alguien más.'
        return message


def setup(bot):
    bot.add_cog(Functions(bot))
